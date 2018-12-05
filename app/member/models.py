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
    # TODO: foreign key로 엮을것인가?
    consumer_idx = models.PositiveIntegerField(
        '소비자_idx', blank=True, null=True,
    )
    # TODO: foreign key로 엮을것인가?
    photographer_idx = models.PositiveIntegerField(
        '사진작가_idx', blank=True, null=True,
    )

    def save(self, *args, **kwargs):
        super(Member, self).save(*args, **kwargs)
        if self.member_type == 0:  # 소비자
            consumer = Consumer(member_idx=self.pk, contracts=[])
            consumer.save()
            self.consumer_idx = consumer.pk
        else:  # 사진작가
            photographer = Photographer(member_idx=self.pk, markets=[])
            photographer.save()
            self.photographer_idx = photographer.pk
        super(Member, self).save(*args, **kwargs)


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
