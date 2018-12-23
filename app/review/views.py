from django.http import HttpResponse
from django.shortcuts import render, redirect

from market.models import Market
from member.models import Member
from review.forms import ReviewForm


def review_add_view(request, pk):
    user = request.user
    member = Member.objects.get(pk=user.id)
    market = Market.objects.get(pk=pk)
    form = ReviewForm()

    if not user.is_authenticated:
        return HttpResponse(status=403)
    if member.member_type != 0:
        return HttpResponse(status=401)

    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.market_idx = market.id
            review.reviewer_idx = member.consumer_idx
            review.reviewer_name = member.username
            review.save()

            market.stars += review.stars
            market.save()
            return redirect('market_post', pk=pk)

    context = {'form': form, 'market': market}
    return render(request, 'review/add.html', context=context)


def review_edit_view(request, pk):
    pass


def review_retrieve_view(request, pk):
    pass


def review_market_view(request, pk):
    pass
