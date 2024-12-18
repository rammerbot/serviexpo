from django.db import models

# Create your models here.

class Experience(models.Model):

    date = models.DateField('Fecha', blank=True)
    service = models.CharField('Servicio', max_length=70, blank=True)
    position = models.CharField('Cargo', max_length=50, blank=True)
    company = models.CharField('Compañia', max_length=100)
    description = models.TextField('Description')
    image = models.ImageField('Imagen', upload_to='experiencia/')

    class Meta:
        verbose_name = ('Experiencia')
        verbose_name_plural = ('Experiencias')

    def __str__(self):
        return self.company
    
class Education(models.Model):
    date = models.DateField('Fecha')
    institute = models.CharField('Instituto', max_length=150)
    title = models.CharField('Titulo', max_length=150, blank=True)
    url = models.URLField('URL Certificado', blank=True)
    image = models.ImageField('Imagen', upload_to='project/', blank=True)
    description = models.TextField('Descripcion')

    class Meta:
        verbose_name = ('Educacion')
        verbose_name_plural = ('Educaciones')

    def __str__(self):
        return self.institute
    
class Skill(models.Model):
    skill = models.CharField('Habilidad 1',max_length =100)
    img = models.ImageField('Imagen', upload_to='Habilidades/', blank = True)

    class Meta:
        verbose_name = ('Habilidad')
        verbose_name_plural = ('Habilidades')

    def __str__(self):
        return self.skill
    
class Technology(models.Model):
    technology = models.CharField('Tecnologia 1', max_length = 100)
    img = models.ImageField('Imagen', upload_to='Tecnologia/', blank = True)

    class Meta:
        verbose_name = ('Tecnologia')
        verbose_name_plural = ('Tecnologias')

    def __str__(self):
        return self.technology