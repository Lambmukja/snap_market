from django import forms

from market.models import Market
from tag.models import Tag


class MarketForm(forms.ModelForm):
    posts = forms.CharField(label='게시글', widget=forms.Textarea, required=False)
    tags = forms.MultipleChoiceField(
        label='태그',
        choices=[(ele.pk, ele.tag) for ele in Tag.objects.all().order_by('id')],
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    def clean(self):
        studio_name = self.cleaned_data.get('studio_name')
        if Market.objects.filter(studio_name__exact=studio_name):
            self.add_error('studio_name', "중복된 스튜디오 이름입니다.")
        return self.cleaned_data

    class Meta:
        model = Market
        fields = ('studio_name', 'location', 'working_time', 'posts', 'costs', 'photo',
                  'phone', 'kakao_id',)
