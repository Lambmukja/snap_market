from rest_framework import serializers

from member.models import Photographer


class PhotographerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographer
        fields = (
            'id', 'markets', 'member_idx',
        )
