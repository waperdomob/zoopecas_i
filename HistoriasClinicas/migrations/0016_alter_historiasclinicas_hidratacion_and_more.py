# Generated by Django 4.0.4 on 2023-11-22 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HistoriasClinicas', '0015_alter_seguimiento_observaciones_documentosad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiasclinicas',
            name='hidratacion',
            field=models.FloatField(help_text='(%)'),
        ),
        migrations.AlterField(
            model_name='historiasclinicas',
            name='observaciones',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='observaciones',
            field=models.TextField(),
        ),
    ]
