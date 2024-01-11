# Generated by Django 5.0.1 on 2024-01-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=70, verbose_name='Empresa')),
                ('service_1', models.CharField(max_length=50, verbose_name='Servicio 1')),
                ('service_2', models.CharField(max_length=50, verbose_name='Servicio 2')),
                ('service_3', models.CharField(max_length=50, verbose_name='Servicio 3')),
                ('slogan', models.CharField(max_length=150, verbose_name='Slogan corto')),
                ('slogan_1', models.CharField(max_length=255, verbose_name='Slogan largo')),
                ('about', models.TextField(verbose_name='Sobre Nosotros')),
                ('image', models.ImageField(upload_to='empresa/', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Home',
                'verbose_name_plural': 'Homes',
            },
        ),
    ]
