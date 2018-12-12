from django.shortcuts import render, redirect

from contract.forms import ContractForm
from contract.models import Contract
from market.models import Market
from member.models import Member, Consumer


def mixin_contract_view(request, pk):
    contract = Contract.objects.get(pk=pk)
    if request.method == 'GET':
        pass
    context = {"contract": contract}
    return render(request, "", context)


def create_contract_view(request, market_id):
    form = ContractForm()
    member = Member.objects.get(pk=request.user.id)
    consumer = Consumer.objects.get(pk=member.pk)
    market = Market.objects.get(pk=market_id)
    if request.method == 'POST':
        form = ContractForm(data=request.POST)
        if form.is_valid():
            contract = form.save()
            consumer.contracts.append(contract.pk)
            market.contract_idxs.append(contract.pk)

            market.save()
            consumer.save()
            return redirect("market_post")

    context = {"form": form, "market": market, "consumer": consumer}
    return render(request, "", context)
