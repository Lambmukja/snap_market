from django.shortcuts import render

from market.models import Market


def market_post_view(request, pk):
    market = Market.objects.get(pk=pk)
    context = {"market": market}
    return render(request, "market/post.html", context)
