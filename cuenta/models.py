from django.db import models

# create your models here

class divisional(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre

class estado(models.Model):
    nombre = models.CharField(max_length=30)
    divisional =  models.ForeignKey(divisional, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre

class ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    estado =  models.ForeignKey(estado, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre

class central(models.Model):
    nombre = models.CharField(max_length=40)
    ciudad =  models.ForeignKey(ciudad, on_delete=models.CASCADE)
    direccion = models.TextField(blank=True, null=True)
    localizacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre

class cluster_ce(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre