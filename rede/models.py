from django.db import models

# Create your models here.
from rede import choices


# Criação dos models, com migrate foi criado no Database

class Poste(models.Model):
    id_poste = models.CharField(db_column='id_poste', max_length=20, null=False, primary_key=True)
    tipo_poste = models.SmallIntegerField(db_column='ic_tipo_post', choices=choices.TIPO_POSTE)

    class Meta:
        managed = True
        db_table = '"volare"."tbl_poste"'


class Ligacao(models.Model):
    id_ligacao = models.CharField(db_column='id_ligacao', max_length=20, null=False, primary_key=True)
    id_poste_origem = models.ForeignKey(Poste, db_column='id_poste_origem', max_length=20, null=False, blank=True,
                                        on_delete=models.CASCADE, related_name='poste_origem')
    id_poste_destino = models.ForeignKey(Poste, db_column='id_poste_destino', max_length=20, null=False, blank=True,
                                         on_delete=models.CASCADE, related_name='post_destino')

    distancia = models.DecimalField(db_column='vl_distancia', null=False, decimal_places=2, max_digits=12)

    class Meta:
        managed = True
        db_table = '"volare"."tbl_ligacao"'
