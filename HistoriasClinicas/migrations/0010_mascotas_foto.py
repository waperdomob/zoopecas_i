# Generated by Django 4.0.4 on 2022-06-01 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HistoriasClinicas', '0009_alter_historiasclinicas_inspeccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascotas',
            name='foto',
            field=models.ImageField(null=True, upload_to='mascotas/'),
        ),
    ]
