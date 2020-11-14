from rest_framework import generics

from ccas.models import Cca
from ccas.serializers import CcaSerializer


class CcaList(generics.ListCreateAPIView):
    queryset = Cca.objects.all()
    serializer_class = CcaSerializer


class CcaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cca.objects.all()
    serializer_class = CcaSerializer
