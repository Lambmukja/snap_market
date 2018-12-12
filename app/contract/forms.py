from django import forms

from contract.models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ("consumer_idx", "market_idx", "start_time", "end_time")
