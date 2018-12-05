from rest_framework import serializers

from member.models import Photographer, Consumer


class PhotographerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographer
        fields = (
            'id', 'markets', 'member_idx',
        )


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = (
            'id', 'member_idx',
        )
