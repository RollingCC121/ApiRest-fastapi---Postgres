from django.db import models


class MiErrorModelo(Exception):
    def __init__(self, message):
        self.message = message

class model_autobus(models.Model):
    id_autobus = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=50, unique=True)
    marca = models.CharField(max_length=100)
    ruta = models.CharField(max_length=100)

    def __str__(self):
        return self.placa

class model_horario(models.Model):
    id_horario = models.AutoField(primary_key=True)
    hora = models.TimeField()
    hora_pico = models.CharField(max_length=3)

    def __str__(self):
        return str(self.hora)

class model_programacion_autobuses(models.Model):
    id_programacion_autobuses = models.AutoField(primary_key=True)
    autobus_fk = models.ForeignKey(model_autobus, on_delete=models.CASCADE)
    horario_fk = models.ForeignKey(model_horario, on_delete=models.CASCADE)

class model_cargador(models.Model):
    id_cargador = models.AutoField(primary_key=True)
    autobus_fk = models.ForeignKey(model_autobus, on_delete=models.CASCADE)

class model_programacion_cargadores(models.Model):
    id_programacion_cargadores = models.AutoField(primary_key=True)
    horario_fk = models.ForeignKey(model_horario, on_delete=models.CASCADE)
    autobus_fk = models.ForeignKey(model_autobus, on_delete=models.CASCADE)

