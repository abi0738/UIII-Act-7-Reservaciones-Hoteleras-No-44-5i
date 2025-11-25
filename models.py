from django.db import models

# ============================
# CLIENTE
# ============================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


# ============================
# HABITACIÓN
# ============================
class Habitacion(models.Model):
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    precio_noche = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"Habitación {self.numero}"


# ============================
# RESERVA
# ============================
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reserva {self.id}"


# ============================
# PAGO
# ============================
class Pago(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    fecha_pago = models.DateField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"Pago {self.id}"


# ============================
# EMPLEADO
# ============================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    turno = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
