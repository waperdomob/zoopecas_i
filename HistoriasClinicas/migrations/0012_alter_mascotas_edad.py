# Generated by Django 4.0.4 on 2022-06-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HistoriasClinicas', '0011_alter_mascotas_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='edad',
            field=models.DateField(null=True),
        ),
    ]
