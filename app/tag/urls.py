from django.urls import path

from tag.views import tag_search_view, tag_recommend_view

urlpatterns = [
    path('<int:pk>/', tag_search_view, name='tag_search'),
    path('recommend/', tag_recommend_view, name='tag_recommend'),
]
