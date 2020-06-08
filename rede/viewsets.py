from rest_framework import viewsets

from rede.filters import LigacaoFilterSet
from rede.serializers import *


class PosteViewSets(viewsets.ModelViewSet):
    serializer_class = PosteSerializer
    queryset = Poste.objects.all()


class LigacaoViewSets(viewsets.ModelViewSet):
    serializer_class = LigacaoSerializer
    queryset = Ligacao.objects.all()

    # Filter para verificar as conectividades
    filter_class = LigacaoFilterSet
