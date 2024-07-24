from django.db import models

# Create your models here.


class Project(models.Model):
    project = models.CharField('Proyecto',max_length=100)
    resume = models.TextField('Resumen')
    image = models.ImageField('Imagen', upload_to='project/')
    url = models.URLField('Direccion Web', blank=True)
    repository = models.URLField('Repositorio', blank=True)
    
    class Meta:
        verbose_name = ('Proyecto')
        verbose_name_plural = ('Proyectos')

    def __str__(self):
        return self.project