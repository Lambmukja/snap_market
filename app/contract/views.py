from django.shortcuts import render, redirect

from contract.forms import ContractForm
from contract.models import Contract
from market.models import Market
from member.models import Member, Consumer


def contract_page_view(request, pk):
    contract = Contract.objects.get(pk=pk)
    market = Market.objects.get(pk=contract.market_idx)
    member = Member.objects.get(consumer_idx=contract.consumer_idx)
    if request.method != 'GET':
        pass
    context = {
        "contract": contract,
        "market": market,
        "consumer_name": member.username,
    }
    return render(request, "contract/page.html", context)


def create_contract_view(request, market_id):
    form = ContractForm()
    member = Member.objects.get(pk=request.user.id)
    consumer = Consumer.objects.get(pk=member.consumer_idx)
    market = Market.objects.get(pk=market_id)
    if request.method == 'POST':
        form = ContractForm(data=request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.consumer_idx = consumer.pk
            contract.market_idx = market.pk
            contract.cost = market.costs
            contract.save()
            consumer.contracts.append(contract.pk)
            market.contract_idxs.append(contract.pk)

            market.save()
            consumer.save()
            return redirect("market_post", pk=market_id)

    context = {"form": form, "market": market, "consumer": consumer}
    return render(request, "contract/create.html", context)
