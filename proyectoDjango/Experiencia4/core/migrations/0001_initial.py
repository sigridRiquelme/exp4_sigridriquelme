# Generated by Django 3.2.5 on 2021-07-08 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='colaboradores',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('telefono', models.CharField(max_length=9, verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('pais', models.CharField(max_length=30, verbose_name='Pais')),
            ],
        ),
    ]
