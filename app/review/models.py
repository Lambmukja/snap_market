from django.db import models

CHOICES = {
    '별점': [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
}


# Create your models here.
class Review(models.Model):
    # 소비자 idx
    reviewer_idx = models.PositiveSmallIntegerField(blank=False, null=False)
    reviewer_name = models.CharField(max_length=150, blank=False, null=False, default='익명')
    market_idx = models.PositiveSmallIntegerField(blank=False, null=False)
    stars = models.PositiveSmallIntegerField(
        '별점', choices=CHOICES['별점'],
    )
    review = models.TextField("리뷰")
