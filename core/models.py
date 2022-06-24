from django.db import models

# Create your models here.
'''
•	id_cliente (PK, Integer, verbose name = Identificador del cliente)
•	nombre (String, largo máximo 100, No nulo, verbose name = Nombre del cliente)
•	apellidos (String, largo máximo 150, No nulo, verbose name = Apellido del cliente)
•	correo (String, largo máximo 200, No nulo, verbose name = Correo del cliente).
•	dirección (String, largo máximo 200, verbose name = Dirección del cliente)
'''
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, verbose_name="Identificador del cliente")
    nombre     = models.CharField(max_length=100, null=False, verbose_name='Nombre del cliente')
    apellidos  = models.CharField(max_length=150, null=False, verbose_name='Apellido del cliente')
    correo     = models.CharField(max_length=200, null=False, verbose_name='Correo del cliente')
    dirección  = models.CharField(max_length=200, null=True, verbose_name='Dirección del cliente')

    def __str__(self):
        return self.nombre