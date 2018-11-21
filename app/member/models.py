from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

CHOICES = {
    '회원종류': [(0, '소비자'), (1, '사진작가')]
}


class Member(User):
    member_type = models.PositiveSmallIntegerField(
        '회원종류', choices=CHOICES['회원종류'],
    )
    consumer_idx = models.PositiveIntegerField(
        '소비자_idx', blank=True, null=True,
    )
    photographer_idx = models.PositiveIntegerField(
        '사진작가_idx', blank=True, null=True,
    )


class Consumer(models.Model):
    member_idx = models.PositiveIntegerField(
        '회원정보_idx', blank=True, null=True,
    )
    contracts = ArrayField(models.PositiveIntegerField())


class Photographer(models.Model):
    markets = ArrayField(models.PositiveIntegerField())
    member_idx = models.PositiveIntegerField(
        '회원정보_idx', blank=True, null=True,
    )
