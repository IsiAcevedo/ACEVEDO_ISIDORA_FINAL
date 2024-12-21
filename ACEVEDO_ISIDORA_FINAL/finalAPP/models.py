from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=80, unique=True)  # Nombre de la institución
 

    def __str__(self):
        return self.nombre

class Participante(models.Model):
    RESERVADO = 'RESERVADO'
    COMPLETADA = 'COMPLETADA'
    ANULADA = 'ANULADA'
    NO_ASISTEN = 'NO_ASISTEN'

    ESTADO_CHOICES = [
        (RESERVADO, 'Reservado'),
        (COMPLETADA, 'Completada'),
        (ANULADA, 'Anulada'),
        (NO_ASISTEN, 'No Asisten'),
    ]

    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name="participantes") 
    nro_personas = models.PositiveIntegerField()
    telefono = models.CharField(max_length=15)
    fecha_inscripcion = models.DateField()
    hora_inscripcion = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default=RESERVADO)
    observaciones = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.id} - {self.institucion.nombre}"
