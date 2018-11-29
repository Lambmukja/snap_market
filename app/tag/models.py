from django.db import models

CHOICES = {
    '태그타입': [(0, '장소'), (1, '분위기')]
}


# Create your models here.
class Tag(models.Model):
    tag_type = models.PositiveSmallIntegerField(
        '태그 타입', choices=CHOICES['태그타입'],
    )
    tag = models.CharField('태그', max_length=10, null=False, blank=False)
    reference = models.PositiveIntegerField(blank=False, null=False, default=0)
    weight = models.FloatField(blank=False, null=False, default=0.)

