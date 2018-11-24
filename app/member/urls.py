from django.conf.urls import url

from app.member.views import signup_view, login_view

urlpatterns = [
    url(r'^signup/$', signup_view, name='member_signup'),
    url(r'^login/$', login_view, name='member_login'),
]
