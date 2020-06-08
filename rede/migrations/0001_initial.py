# Generated by Django 3.0.7 on 2020-06-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ligacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ligacao', models.CharField(db_column='id_ligacao', max_length=20)),
                ('id_poste_origem', models.CharField(db_column='id_poste_origem', max_length=20)),
                ('id_poste_destino', models.CharField(db_column='id_poste_destino', max_length=20)),
                ('distancia', models.DecimalField(db_column='vl_distancia', decimal_places=2, max_digits=12)),
            ],
            options={
                'db_table': '"volare"."tbl_ligacao"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_poste', models.CharField(db_column='id_poste', max_length=20)),
                ('tipo_poste', models.SmallIntegerField(choices=[(0, 'Madeira'), (1, 'Concreto')], db_column='ic_tipo_post')),
            ],
            options={
                'db_table': '"volare"."tbl_poste"',
                'managed': True,
            },
        ),
    ]
