from django.http import HttpResponse
from django.shortcuts import render, redirect

from market.forms import MarketForm
from market.models import Market
from member.models import Member, Photographer
from tag.models import Tag


def market_post_view(request, pk):
    market = Market.objects.get(pk=pk)
    tags = Tag.objects.filter(pk__in=market.tags)
    context = {"market": market, "tags": tags}
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
            print(tags)
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
