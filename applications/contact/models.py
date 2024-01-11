from django.db import models
from applications.home.models import Home

# Create your models here.


class SocialMedia(models.Model):
    company = models.ForeignKey(Home, on_delete=models.CASCADE)
    facebook = models.URLField('Facebook', blank=True)
    instagram = models.URLField('Instagram', blank=True)
    x = models.URLField('X', blank=True)
    github = models.URLField('GitHub', blank=True)
    linkedin = models.URLField('LinkeDin', blank=True)

    class Meta:
        verbose_name = ('Red Social')
        verbose_name_plural = ('Redes Sociales')
    def __str__(self):
        return self.company.company

class Contact(models.Model):

    name = models.CharField('Nombre', max_length=50)
    email = models.EmailField('Correo', max_length=50)
    phone = models.CharField('Telefono', max_length=30)
    message = models.TextField('Mensaje')
    date = models.DateTimeField(auto_now_add=True)
 

    class Meta:
        verbose_name = ('Contacto')
        verbose_name_plural = ('Contactos')

    def __str__(self):
        return f"{self.name} {self.date}"
    

