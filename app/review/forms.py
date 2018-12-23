from django import forms

import review
from review.models import Review


class ReviewForm(forms.ModelForm):
    stars = forms.ChoiceField(
        choices=review.models.CHOICES['별점'],
    )

    class Meta:
        model = Review
        fields = ('stars', 'review')
