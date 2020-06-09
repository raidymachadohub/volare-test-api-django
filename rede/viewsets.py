from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rede import actions
from rede.filters import LigacaoFilterSet
from rede.serializers import *


class PosteViewSets(viewsets.ModelViewSet):
    serializer_class = PosteSerializer
    queryset = Poste.objects.all()


class LigacaoViewSets(viewsets.ModelViewSet):
    serializer_class = LigacaoSerializer
    queryset = Ligacao.objects.all()

    # Filter para verificar as conectividades
    # filter_class = LigacaoFilterSet

    @action(methods=['GET'], detail=False)
    def way_perfect(self, request):
        p_origem = request.query_params['p_origem']
        p_destino = request.query_params['p_destino']

        obj = Ligacao.objects.all()

        array = []
        re_grafo = {}

        for x in obj:
            re_grafo.update({x.id_poste_origem_id: [x.id_poste_destino_id]})
            re_grafo.update({x.id_poste_destino_id: [x.id_poste_origem_id]})

        vl = actions.bfs(re_grafo, p_origem, p_destino)
        if vl is not None:
            array.append(vl)
        else:
            array = []
        data = {'conn_way': array}
        return Response(data=data)
