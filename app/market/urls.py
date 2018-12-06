from django.urls import path

from market.views import market_post_view

urlpatterns = [
    path('<int:pk>/', market_post_view, name='market_post'),
]
