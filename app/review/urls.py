from django.urls import path

from review.views import review_add_view, review_edit_view, review_market_view, review_retrieve_view

urlpatterns = [
    path('market/<int:pk>/new/', review_add_view, name='review_add'),
    path('<int:pk>/edit/', review_edit_view, name='review_edit'),
    path('market/<int:pk>/', review_market_view, name='review_market'),
    path('<int:pk>/', review_retrieve_view, name='review_retrieve'),
]
