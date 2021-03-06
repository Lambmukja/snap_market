import os

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models


def get_image_path(instance, filename):
    return os.path.join(settings.MEDIA_ROOT, f"market_{instance.pk:03d}", filename)


# Create your models here.
class Market(models.Model):
    studio_name = models.CharField(
        "스튜디오 이름", max_length=100, blank=False, null=False)
    photographer_idx = models.PositiveSmallIntegerField("사진작가 idx", null=True, blank=True)
    contract_idxs = ArrayField(models.PositiveSmallIntegerField(), null=True, blank=True)

    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    posts = models.TextField("게시글", null=True, blank=True)
    stars = models.PositiveIntegerField("총 별점", default=0)

    # TODO: 나중에 다시 JSONField로 할것. ex) {'월': [(09:00,10:00 <- datetime), ...], ...}
    # working_time = JSONField("영업시간", null=True, blank=True)
    working_time = models.TextField("영업시간", default="", blank=True)
    costs = models.PositiveIntegerField("가격")
    tags = ArrayField(models.PositiveSmallIntegerField(), null=True, blank=True)
    location = models.CharField("위치", max_length=100, blank=True, null=True)

    kakao_id = models.CharField("카카오톡 ID", max_length=50, blank=True, null=True)
    phone = models.CharField("전화번호", max_length=20, blank=True, null=True)
