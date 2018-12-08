from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

import member
from member.models import Member


class MemberForm(UserCreationForm):
    member_type = forms.ChoiceField(
        choices=member.models.CHOICES['회원종류'],
        widget=forms.RadioSelect(),
    )

    class Meta:
        model = Member
        fields = ('member_type', 'username', 'password1', 'password2', 'first_name', 'last_name')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Member.objects.filter(username=username).exists():
            raise forms.ValidationError("이미 존재하는 아이디입니다.")
        return username

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            # TODO: 한글로 표시되지 않음!
            raise forms.ValidationError("두 비밀번호가 일치하지 않습니다.")
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(label='아이디', max_length=255)
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(), max_length=255)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError(
                "아이디 혹은 비밀번호가 일치하지 않습니다."
            )
        return self.cleaned_data
