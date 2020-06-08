from django_filters import filterset
from rede.models import *


class LigacaoFilterSet(filterset.FilterSet):
    p_origem = filterset.CharFilter(field_name='id_poste_origem')
    p_destino = filterset.CharFilter(field_name='id_poste_destino')

    class Meta:
        model = Ligacao
        fields = ['p_origem', 'p_destino']
