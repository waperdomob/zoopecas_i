# Generated by Django 4.0.4 on 2022-04-26 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HistoriasClinicas', '0003_remove_empleados_nombreemp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiasclinicas',
            name='TLIC',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='historiasclinicas',
            name='hidratacion',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='historiasclinicas',
            name='inspeccion',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='historiasclinicas',
            name='peso',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='historiasclinicas',
            name='pulso',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='historiasclinicas',
            name='respiracion',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='historiasclinicas',
            name='temperatura',
            field=models.FloatField(),
        ),
    ]
