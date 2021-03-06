from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from contract.models import Contract
from market.models import Market
from member.forms import MemberForm, LoginForm, ConsumerFavoriteForm
from member.models import Member, Consumer, Photographer
from tag.models import Tag


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

        favorite = Tag.objects.filter(pk__in=consumer.favorite)
        context['favorite'] = favorite
    else:  # 사진작가
        context['member_type'] = '사진작가'
        photographer = Photographer.objects.get(pk=member.photographer_idx)

        markets = Market.objects.filter(pk__in=photographer.markets)
        context['markets'] = markets
        context['contracts'] = {}
        for market in markets:
            context['contracts'][market.studio_name] = Contract.objects.filter(pk__in=market.contract_idxs)

    return render(request, "member/mypage.html", context)


def favorite_edit_view(request):
    user = request.user
    member = Member.objects.get(pk=user.id)
    consumer = Consumer.objects.get(pk=member.consumer_idx)

    if not user.is_authenticated:
        return HttpResponse(status=403)
    if member.member_type != 0:
        return HttpResponse(status=401)

    if request.method == 'POST':
        form = ConsumerFavoriteForm(data=request.POST, instance=consumer)

        if form.is_valid():
            tags = form.cleaned_data.get('favorite')
            tags = [int(tag) for tag in tags]
            consumer.favorite = tags
            consumer.save()
            return redirect('member_mypage')

    elif request.method == 'GET':
        form = ConsumerFavoriteForm(instance=consumer)

    context = {"form": form}
    return render(request, 'member/edit_favorite.html', context)
