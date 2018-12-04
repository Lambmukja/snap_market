from rest_framework import generics

from member.api.serializers import PhotographerSerializer, ConsumerSerializer
from member.models import Photographer, Consumer


class PhotographerListView(generics.ListAPIView):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer


class PhotographerDetailView(generics.RetrieveAPIView):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer


class ConsumerListView(generics.ListAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer


class ConsumerDetailView(generics.RetrieveAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
