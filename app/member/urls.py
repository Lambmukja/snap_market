from django.urls import path

from member.views import signup_view, login_view, logout_view

urlpatterns = [
    path('signup/', signup_view, name='member_signup'),
    path('login/', login_view, name='member_login'),
    path('logout/', logout_view, name='member_logout'),
]
