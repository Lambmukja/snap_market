from django.db import models

CHOICES = {
    '별점': [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
}


# Create your models here.
class Review(models.Model):
    # 소비자 idx
    reviewer_idx = models.PositiveSmallIntegerField(blank=False, null=False)
    market_idx = models.PositiveSmallIntegerField(blank=False, null=False)
    stars = models.PositiveSmallIntegerField(
        '별점', choices=CHOICES['별점'],
    )
    review = models.TextField("리뷰")
