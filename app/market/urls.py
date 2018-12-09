from django.urls import path

from market.views import market_post_view, add_new_market_view

urlpatterns = [
    path('<int:pk>/', market_post_view, name='market_post'),
    path('new/', add_new_market_view, name='market_add'),
]
