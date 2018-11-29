from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models


# Create your models here.
class Market(models.Model):
    studio_name = models.CharField(
        "스튜디오 이름", max_length=100, blank=False, null=False)
    posts = models.TextField("게시글", null=True, blank=True)
    working_time = JSONField("영업시간")
    costs = models.PositiveIntegerField("가격")
    kakao_id = models.CharField("카카오톡 ID", max_length=50, blank=True, null=True)
    photographer_idx = models.PositiveSmallIntegerField("사진작가 idx")
    contract_idxs = ArrayField(models.PositiveSmallIntegerField())
    tags = ArrayField(models.PositiveSmallIntegerField())
    location = models.CharField("위치", max_length=100, blank=True, null=True)
    phone = models.CharField("전화번호", max_length=20, blank=True, null=True)
