from django.urls import path

from tag.views import tag_search_view

urlpatterns = [
    path('<int:pk>/', tag_search_view, name='tag_search'),
]
