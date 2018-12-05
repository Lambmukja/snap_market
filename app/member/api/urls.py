from django.urls import path

from member.api import views

urlpatterns = [
    path('photographers/', views.PhotographerListView.as_view(), name='api_member_photographer_list'),
    path('photographers/<int:pk>/', views.PhotographerDetailView.as_view(), name='api_member_photographer_detail'),
    path('consumers/', views.ConsumerListView.as_view(), name='api_member_consumer_list'),
    path('consumers/<int:pk>/', views.ConsumerDetailView.as_view(), name='api_member_consumer_detail'),
]
