from django.db import models
# Create your models here.


class Info(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.CharField(max_length=14)
    contactado = models.BooleanField(default=False)
    date = models.DateTimeField(null=True)
    tEncargado = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.nombre +' - '+ self.numero

   