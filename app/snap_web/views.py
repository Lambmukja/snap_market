from django.shortcuts import render

from market.models import Market


def home_view(request):
    if request.method == 'GET':
        markets = Market.objects.all()
        posts = []
        for market in markets:
            posts.append({
                'market_id': market.pk,
                'market_name': market.studio_name,
                'market_post': market.posts,
            })
        context = {'posts': posts}
        return render(request, "home.html", context)
