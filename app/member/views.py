from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from member.forms import MemberForm, LoginForm
from member.models import Consumer, Member, Photographer


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, '로그인 하였습니다.')
                return redirect("home")
    context = {'form': form}
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")


def signup_view(request):
    if request.method == 'POST':
        form = MemberForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            member_type = form.cleaned_data.get('member_type')
            form.save()
            member = Member.objects.get(username=username)
            if member_type == 0:  # 소비자
                consumer = Consumer(member_idx=member.pk, contracts=[])
                consumer.save()
                member.consumer_idx = consumer.pk
                member.save()
            else:  # 사진작가
                photographer = Photographer(member_idx=member.pk, markets=[])
                photographer.save()
                member.photographer_idx = photographer.pk
                member.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, 'signup.html', context)
    elif request.method == 'GET':
        form = MemberForm()
    else:
        return HttpResponse(status=405)
    context = {"form": form}
    return render(request, "signup.html", context)
