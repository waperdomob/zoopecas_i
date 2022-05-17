# Generated by Django 4.0.4 on 2022-04-26 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=100)),
                ('cantidad_total', models.IntegerField()),
                ('precio_compra', models.FloatField(max_length=45)),
                ('precio_venta', models.FloatField(max_length=20)),
                ('imagen', models.ImageField(upload_to='')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.categorias')),
            ],
        ),
    ]
