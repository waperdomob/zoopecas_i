# Generated by Django 4.0.4 on 2022-05-31 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HistoriasClinicas', '0008_mascotas_caracteristicas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiasclinicas',
            name='inspeccion',
            field=models.CharField(max_length=100),
        ),
    ]
