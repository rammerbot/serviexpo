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