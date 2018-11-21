from django.conf.urls import url

from app.member.views import signup_view

urlpatterns = [
    url(r'^signup/$', signup_view, name='member_signup'),
]
