from django.shortcuts import render

from market.models import Market
from tag.models import Tag


def market_post_view(request, pk):
    market = Market.objects.get(pk=pk)
    tags = Tag.objects.filter(pk__in=market.tags)
    context = {"market": market, "tags": tags}
    return render(request, "market/post.html", context)
