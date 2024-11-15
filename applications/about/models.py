from django.db import models

# Create your models here.


class AboutPage(models.Model):

    how_we_are = models.TextField('Quienes somos')
    our_mision = models.TextField('Nuesta mision')
    our_projects = models.TextField('Nuestros proyectos')
    our_values = models.TextField('Nuestros Valores')
    why_us = models.TextField('Porque nosotros')

