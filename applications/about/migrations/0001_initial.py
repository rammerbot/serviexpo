# Generated by Django 5.1.3 on 2024-11-15 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_we_are', models.TextField(verbose_name='Quienes somos')),
                ('our_mision', models.TextField(verbose_name='Nuesta mision')),
                ('our_projects', models.TextField(verbose_name='Nuestros proyectos')),
                ('our_values', models.TextField(verbose_name='Nuestros Valores')),
                ('why_us', models.TextField(verbose_name='Porque nosotros')),
            ],
        ),
    ]
