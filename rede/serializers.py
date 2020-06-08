from rest_framework import serializers
from rede.models import *


#Serialização do models

class PosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poste
        fields = '__all__'


class LigacaoSerializer(serializers.ModelSerializer):
    # Relacionamento com as fk's do model POSTE. Apenas leitura

    post_origem_obj = PosteSerializer(source='id_poste_origem', read_only=True)
    post_destino_obj = PosteSerializer(source='id_poste_destino', read_only=True)

    class Meta:
        model = Ligacao
        fields = '__all__'
