from django import forms

from contract.models import Contract


class ContractForm(forms.ModelForm):
    start_time = forms.SplitDateTimeField(label='시작시간',
                                          widget=forms.SplitHiddenDateTimeWidget(
                                              date_format='%Y-%m-%d',
                                              time_format='%H:%M',
                                              date_attrs={'class': 'datepicker'},
                                              time_attrs={'class': 'start_timepicker'}
                                          ))
    end_time = forms.SplitDateTimeField(label='종료시간',
                                        widget=forms.SplitHiddenDateTimeWidget(
                                            date_format='%Y-%m-%d',
                                            time_format='%H:%M',
                                            date_attrs={'class': 'datepicker'},
                                            time_attrs={'class': 'end_timepicker'}
                                        ))

    class Meta:
        model = Contract
        fields = ("start_time", "end_time")

    def clean(self):
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')

        if start_time.date() != end_time.date():
            self.add_error('start_time',
                           "시작날짜와 종료날짜는 같아야합니다.")

        if start_time.time() > end_time.time():
            self.add_error('start_time',
                           "시작날짜의 시간은 종료날짜보다 앞의 시간이여야 합니다.")

        return self.cleaned_data
