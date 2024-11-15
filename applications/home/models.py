from django.db import models

# Create your models here.



class Home(models.Model):
    company = models.CharField('Empresa', max_length=70)
    service_1 = models.CharField("Servicio 1", max_length=50)
    service_2 = models.CharField("Servicio 2", max_length=50)
    service_3 = models.CharField("Servicio 3", max_length=50)
    slogan = models.CharField('Slogan corto', max_length=150)
    slogan_1 = models.CharField('Slogan largo', max_length=255)
    about = models.TextField('Sobre Nosotros')
    image = models.ImageField('Imagen', upload_to='empresa/')

    class Meta:
        verbose_name = ('Home')
        verbose_name_plural = ('Homes')

    def __str__(self):
        return self.company
    
class InfoHome(models.Model):
    first_text = models.TextField('Primer texto')
    second_text = models.TextField('Segundo texto')
    about_me = models.TextField('Sobre mi')
    project_number = models.IntegerField('Cantidad de proyectos')
    experience_number = models.IntegerField('Cantidad de Experience')

    class Meta:
        verbose_name = ('Pagina principal')
        verbose_name_plural = ('Paginas principales')

class Reasons(models.Model):
    reason = models.CharField('Razon', max_length=120)
    description = models.TextField('Descripcion')
    img = models.ImageField('Imagen', upload_to='razones/')
    position = models.IntegerField('Posision', default=0)
    

    def __str__(self):
        return self.reason