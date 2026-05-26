from django.db import models

# Create your models here.
class Alumnos(models.Model):
    ID_Alumno=models.AutoField(primary_key=True)
    DNI=models.TextField(max_length=10)
    Apellido=models.TextField(max_length=35)
    Nombre=models.TextField(max_length=35)
    Edad=models.ImageField()
    Calle=models.TextField(max_length=50)
    Altura=models.ImageField()

    def __str__(self):
        return self.DNI
        