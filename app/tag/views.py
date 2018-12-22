from django.shortcuts import render

from market.models import Market
from tag.models import Tag


def tag_search_view(request, pk):
    markets = Market.objects.filter(tags__contains=[str(pk)])
    tags = Tag.objects.all()
    posts = []
    for market in markets:
        posts.append({
            'market_id': market.pk,
            'market_name': market.studio_name,
            'market_post': market.posts,
            'market_photo': market.photo,
        })
    context = {'posts': posts, 'tags': tags}
    return render(request, "home.html", context)
