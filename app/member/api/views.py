from rest_framework import generics

from member.api.serializers import PhotographerSerializer
from member.models import Photographer


class PhotographerListView(generics.ListCreateAPIView):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer


class PhotographerDetailView(generics.RetrieveAPIView):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer
