from django.urls import path

from member.views import (
    signup_view,
    login_view,
    logout_view,
    mypage_view,
    favorite_edit_view,
)

urlpatterns = [
    path('signup/', signup_view, name='member_signup'),
    path('login/', login_view, name='member_login'),
    path('logout/', logout_view, name='member_logout'),
    path('mypage/', mypage_view, name='member_mypage'),
    path('favorite/edit/', favorite_edit_view, name='favorite_edit'),
]
