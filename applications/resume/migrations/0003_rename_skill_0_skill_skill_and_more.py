# Generated by Django 4.1.3 on 2024-11-15 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_remove_education_certificate_education_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill_0',
            new_name='skill',
        ),
        migrations.RenameField(
            model_name='technology',
            old_name='technology_0',
            new_name='technology',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skill_1',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skill_2',
        ),
        migrations.RemoveField(
            model_name='technology',
            name='technology_1',
        ),
        migrations.RemoveField(
            model_name='technology',
            name='technology_2',
        ),
        migrations.AddField(
            model_name='skill',
            name='img',
            field=models.ImageField(blank=True, upload_to='Habilidades/', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='technology',
            name='img',
            field=models.ImageField(blank=True, upload_to='Tecnologia/', verbose_name='Imagen'),
        ),
    ]
