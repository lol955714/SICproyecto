from django.db import models

# Create your models here.
class Empresa(models.Model):
	nombre = models.CharField(max_length=15)
	direccion= models.CharField(max_length=15)
	telefono = models.CharField(max_length=15)
	nit = models.CharField(max_length=15)
	codigo= models.CharField(max_length=15)
	def __str__(self):
		return '%i'%(self.nombre)

class Categoría(models.Model):
	codigo=models.CharField(max_length=10)
	nombre=models.CharField(max_length=10)
	def __str__(self):
		return '%i'&(self.nombre)

class Factura(models.Model):
	fkEmpresa=models.ForeignKey(Empresa,on_delete=models.CASCADE)
	codigo=models.IntegerField()
	fecha=models.DateTimeField(auto_now=True)
	total = models.DecimalField(max_digits=6,decimal_places=2)
	iva=models.DecimalField(max_digits=4,decimal_places=2)
	retencion=models.DecimalField(max_digits=4,decimal_places=2)
	def __str__(self):
		return '%i'&(self.codigo)

class Producto(models.Model):
	fkCategoría=models.ForeignKey(Categoría,on_delete=models.CASCADE)
	codigo=models.CharField(max_length=15)
	nombre = models.CharField(max_length=15)
	existencia=models.IntegerField()
	def __str__(self):
		return '%i'&(self.nombre)

class LineaDeVenta(models.Model):
	fkFactura=models.ForeignKey(Factura,on_delete=models.CASCADE)
	fkProducto=models.ForeignKey(Producto,on_delete=models.CASCADE)
	cantidad=models.IntegerField(default=1)
	subtotal=models.DecimalField(max_digits=6,decimal_places=2)
	def __str__(self):
		return '%i'&(self.id)

class CategoriaCuentas(models.Model):
	tipo=models.IntegerField()
	nombre=models.CharField(max_length=10)
	def __str__(self):
		return '%i'&(self.nombre)

##Opción 1
class Cuenta(models.Model):
	nombre=models.CharField(max_length=15)
	fkCategoria=models.ForeignKey(CategoriaCuentas,on_delete=models.CASCADE)
	debe=models.DecimalField(max_digits=6,decimal_places=2)
	haber=models.DecimalField(max_digits=6,decimal_places=2)
	def __str__(self):
		return '%i'&(self.nombre)

##opción 2
#opté por la segunda opción dado que habrán * registros debe/haber
class RegistroHaber(models.Model):
	fkCuenta=models.ForeignKey(Cuenta,on_delete=models.CASCADE)
	monto=models.DecimalField(max_digits=6,decimal_places=2)


class RegistroDebe(models.Model):
	fkCuenta=models.ForeignKey(Cuenta,on_delete=models.CASCADE)
	monto=models.DecimalField(max_digits=6,decimal_places=2)


class Transaccion(models.Model):
	fkRegistroHaber=models.ForeignKey(RegistroHaber,on_delete=models.CASCADE)
	fkRegistroDebe=models.ForeignKey(RegistroDebe,on_delete=models.CASCADE)
	fecha=models.DateTimeField(auto_now=True)
