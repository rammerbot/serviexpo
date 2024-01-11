from django.db import models

# Create your models here.


class Project(models.Model):
    project = models.CharField('Proyecto',max_length=100)
    resume = models.TextField('Resumen')
    image = models.ImageField('Imagen', upload_to='project/')
    
    class Meta:
        verbose_name = ('Proyecto')
        verbose_name_plural = ('Proyectos')

    def __str__(self):
        return self.project