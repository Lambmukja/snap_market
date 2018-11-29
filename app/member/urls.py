from django.urls import path

from member.views import signup_view, login_view

urlpatterns = [
    path('signup/', signup_view, name='member_signup'),
    path('login/', login_view, name='member_login'),
]
