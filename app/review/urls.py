from django.urls import path

from review.views import review_add_view

urlpatterns = [
    path('market/<int:pk>/new/', review_add_view, name='review_add'),
]
