from django.contrib.auth.forms import UserCreationForm

from app.member.models import Member


class MemberForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name',)
