from django.shortcuts import render

from market.models import Market
from member.models import Member
from tag.models import Tag


def home_view(request):
    if request.method == 'GET':
        is_consumer = False
        if request.user.is_authenticated:
            member = Member.objects.get(pk=request.user.id)
            if member.member_type == 0:
                is_consumer = True

        markets = Market.objects.all()
        tags = Tag.objects.all()
        posts = []
        for market in markets:
            posts.append({
                'market_id': market.pk,
                'market_name': market.studio_name,
                'market_post': market.posts,
                'market_photo': market.photo,
            })
        context = {
            'posts': posts,
            'tags': tags,
            'cur_tag': None,
            'is_consumer': is_consumer,
        }
        return render(request, "home.html", context)
