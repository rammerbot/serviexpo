# Generated by Django 4.1.3 on 2024-11-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='repository',
            field=models.URLField(blank=True, verbose_name='Repositorio'),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, verbose_name='Direccion Web'),
        ),
    ]
