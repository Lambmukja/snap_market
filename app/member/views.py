from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.member.forms import MemberForm, LoginForm


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


def signup_view(request):
    if request.method == 'POST':
        form = MemberForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home")
    elif request.method == 'GET':
        form = MemberForm()
    else:
        return HttpResponse(status=405)
    context = {"form": form}
    return render(request, "signup.html", context)


def home_view(request):
    if request.method == 'GET':
        return render(request, "home.html")
