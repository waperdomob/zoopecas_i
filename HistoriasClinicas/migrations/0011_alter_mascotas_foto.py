# Generated by Django 4.0.4 on 2022-06-07 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HistoriasClinicas', '0010_mascotas_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='mascotas/'),
        ),
    ]
