from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from contract.models import Contract
from market.models import Market
from member.forms import MemberForm, LoginForm, MarketForm
from member.models import Member, Consumer, Photographer


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
            form.save()
            username = form.cleaned_data.get('username')
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


def mypage_view(request):
    user = request.user
    if request.method != 'GET':
        return HttpResponse(status=405)
    if not user.is_authenticated:
        return HttpResponse(status=403)
    context = {'member_name': user.username}

    member = Member.objects.get(pk=user.id)
    if member.member_type == 0:  # 소비자
        context['member_type'] = '소비자'
        consumer = Consumer.objects.get(pk=member.consumer_idx)

        contracts = Contract.objects.filter(pk__in=consumer.contracts)
        context['contracts'] = contracts
    else:  # 사진작가
        context['member_type'] = '사진작가'
        photographer = Photographer.objects.get(pk=member.photographer_idx)

        markets = Market.objects.filter(pk__in=photographer.markets)
        context['markets'] = markets
        context['contracts'] = {}
        for market in markets:
            context['contracts'][market.studio_name] = Contract.objects.filter(pk__in=market.contract_idxs)

    return render(request, "member/mypage.html", context)


def mypage_add_market_view(request):
    if request.method == 'POST':
        form = MarketForm(data=request.POST)
        # TODO: form에 등록된 것 DB에 저장하기
    elif request.method == 'GET':
        form = MarketForm()
    else:
        return HttpResponse(status=405)
    context = {"form": form}
    return render(request, "member/mypage_add_market.html", context)
