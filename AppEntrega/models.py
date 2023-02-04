from django.db import models

class Series(models.Model):

    nombre=models.CharField(max_length=40)
    valoracion=models.CharField(max_length=300)

    def __str__(self):
        return f"Nombre: {self.nombre} - Valoracion: {self.valoracion}"

class Peliculas(models.Model):
    
    nombre= models.CharField(max_length=30)
    duracion= models.CharField(max_length=30)
    critica= models.CharField(max_length=300)

    def __str__(self):
        return f"Nombre: {self.nombre} - Critica: {self.critica}"

class Premios(models.Model):

    pelicula= models.CharField(max_length=30)
    premio= models.CharField(max_length=30)
    año= models.IntegerField()

    def __str__(self):
        return f"Pelicula: {self.pelicula} - Premio: {self.premio}"



