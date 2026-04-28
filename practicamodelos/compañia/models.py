from django.db import models

class Salario(models.Model):
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank = False, null = False)
    aguinaldo = models.DecimalField(max_digits=10, decimal_places=2, blank = False, null = False)

    def __str__(self):
        return self.salario
    
class Pais(models.Model):
    pais = models.CharField(max_length=100, blank = False, null = False)
    
    def __str__(self):
        return self.pais

class Localizacion(models.Model):
    localizacion = models.CharField(max_length=100, blank = False, null = False)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, blank = False, null = False)

    def __str__(self):
        return self.localizacion

class Fabrica(models.Model):
    localizacion = models.ForeignKey(Localizacion, on_delete=models.CASCADE, blank = False, null = False)

    def __str__(self):
        return self.localizacion
    
class Puesto(models.Model):
    puesto = models.CharField(max_length=100, blank = False, null = False)
    salario = models.ForeignKey(Salario, on_delete=models.CASCADE, blank = False, null = False)

    def __str__(self):
        return self.puesto

class Empleado(models.Model):
    nombre = models.CharField(max_length=100, blank = False, null = False)
    apellido = models.CharField(max_length=100, blank = False, null = False)
    cedula = models.CharField(max_length=10, blank = False, null = False)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE, blank = False, null = False)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, blank = False, null = False)
    def __str__(self):
        return self.nombre + " " + self.apellido
    


    

