from django.shortcuts import render

from market.models import Market
from member.models import Member, Consumer
from review.models import Review
from tag.models import Tag
from tag.recommend.recommend import recommend


def tag_search_view(request, pk):
    is_consumer = False
    if request.user.is_authenticated:
        member = Member.objects.get(pk=request.user.id)
        if member.member_type == 0:
            is_consumer = True

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
    context = {'posts': posts, 'tags': tags, 'cur_tag': pk, 'is_consumer': is_consumer}
    return render(request, "home.html", context)


def tag_recommend_view(request):
    """
    search type: review, star, favorite
    """
    tags = Tag.objects.all()
    is_consumer = False
    if request.user.is_authenticated:
        member = Member.objects.get(pk=request.user.id)
        if member.member_type == 0:
            is_consumer = True

    if not is_consumer:
        markets = Market.objects.all()
        posts = []
        for market in markets:
            posts.append({
                'market_id': market.pk,
                'market_name': market.studio_name,
                'market_post': market.posts,
                'market_photo': market.photo,
            })
        context = {'posts': posts, 'tags': tags, 'cur_tag': None, 'is_consumer': is_consumer}
        return render(request, "home.html", context)

    search = request.GET.get('search')
    if not search:
        search = 'review'

    sorted_markets = []
    if search == 'review':
        markets = Market.objects.all()
        for market in markets:
            count = Review.objects.filter(market_idx=market.id).count()
            sorted_markets.append((market, count))
        sorted_markets = sorted(sorted_markets, key=lambda x: x[1], reverse=True)
    elif search == 'star':
        markets = Market.objects.all()
        for market in markets:
            count = Review.objects.filter(market_idx=market.id).count()
            avg_stars = 0
            if count > 0:
                avg_stars = market.stars / count
            sorted_markets.append((market, avg_stars))
        sorted_markets = sorted(sorted_markets, key=lambda x: x[1], reverse=True)
    elif search == 'favorite':
        member = Member.objects.get(pk=request.user.id)
        consumer = Consumer.objects.get(pk=member.consumer_idx)
        sorted_markets = recommend(consumer.favorite)

    posts = []
    for market, score in sorted_markets:
        # For score debugging
        # print(f"market name: {market.studio_name}, score: {score}")
        posts.append({
            'market_id': market.id,
            'market_name': market.studio_name,
            'market_post': market.posts,
            'market_photo': market.photo,
        })

    context = {
        'posts': posts,
        'tags': tags,
        'cur_tag': "추천",
        'is_consumer': is_consumer,
        'search': search,
    }
    return render(request, "home.html", context)
