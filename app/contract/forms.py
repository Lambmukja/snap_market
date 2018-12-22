from django import forms

from contract.models import Contract


class ContractForm(forms.ModelForm):
    start_time = forms.SplitDateTimeField(label='시작시간',
                                          widget=forms.SplitHiddenDateTimeWidget(
                                              date_format='%Y-%m-%d',
                                              time_format='%H:%M',
                                              date_attrs={'class':'datepicker'},
                                              time_attrs={'class':'start_timepicker'}
                                          ))
    end_time = forms.SplitDateTimeField(label='종료시간',
                                        widget=forms.SplitHiddenDateTimeWidget(
                                            date_format='%Y-%m-%d',
                                            time_format='%H:%M',
                                            date_attrs={'class':'datepicker'},
                                            time_attrs={'class':'end_timepicker'}
                                        ))

    class Meta:
        model = Contract
        fields = ("start_time", "end_time")
