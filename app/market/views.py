from django.http import HttpResponse
from django.shortcuts import render, redirect

from contract.models import Contract
from market.forms import MarketForm
from market.models import Market
from member.models import Member, Photographer, Consumer
from review.models import Review
from tag.models import Tag


def market_post_view(request, pk):
    user = request.user

    market = Market.objects.get(pk=pk)
    member = Member.objects.get(pk=user.id)
    tags = Tag.objects.filter(pk__in=market.tags)
    reviews = Review.objects.filter(market_idx=pk)
    avg_stars = 0
    if len(reviews):
        avg_stars = f"{(market.stars / len(reviews)):.1f}"

    is_consumer = True if member.member_type == 0 else False

    context = {
        "is_consumer": is_consumer,
        "market": market,
        "tags": tags,
        "reviews": reviews,
        "avg_stars": avg_stars,
    }

    if user.is_authenticated:
        if is_consumer:  # 소비자
            context['user_type'] = 'consumer'
            context['consumer_contract'] = []
            consumer = Consumer.objects.get(pk=member.consumer_idx)
            contract_idxs = consumer.contracts
            for idx in contract_idxs:
                contract = Contract.objects.get(pk=idx)
                if contract.market_idx == market.pk:
                    context['consumer_contract'].append(contract)

        else:  # 사진작가
            context['user_type'] = 'nothing'
            if member.photographer_idx == market.photographer_idx:
                context['user_type'] = 'photographer'
                context['total_contracts'] = len(market.contract_idxs)
                context['photographer_contract'] = {}
                for idx in market.contract_idxs:
                    contract = Contract.objects.get(pk=idx)
                    consumer = Consumer.objects.get(pk=contract.consumer_idx)
                    username = Member.objects.get(pk=consumer.member_idx).username
                    context['photographer_contract'].setdefault(username, []).append(contract)

    return render(request, "market/post.html", context)


def add_new_market_view(request):
    if request.method == 'POST':
        user = request.user
        form = MarketForm(data=request.POST, files=request.FILES)
        # TODO: form에 등록된 것 DB에 저장하기
        if form.is_valid():
            market = form.save(commit=False)
            photo = market.photo
            market.photo = None
            market.save()

            # To get pk of market at image saving
            market.photo = photo
            market.save()
            tags = form.cleaned_data.get('tags')
            tags = [int(tag) for tag in tags]
            for tag_idx in tags:
                tag = Tag.objects.get(pk=tag_idx)
                tag.reference += 1
                tag.save()

            market.tags = tags
            market.contract_idxs = []
            member = Member.objects.get(pk=user.id)
            photographer = Photographer.objects.get(pk=member.photographer_idx)
            photographer.markets.append(market.pk)
            photographer.save()
            market.photographer_idx = photographer.pk
            market.save()
            return redirect("member_mypage")
    elif request.method == 'GET':
        form = MarketForm()
    else:
        return HttpResponse(status=405)
    context = {"form": form}
    return render(request, "market/add.html", context)
