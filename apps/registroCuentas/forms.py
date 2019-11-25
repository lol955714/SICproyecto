from django import forms

from apps.informesContables.models import Cuenta, Transaccion, RegistroDebe, RegistroHaber

from django.forms import fields

class CuentaForm(forms.ModelForm):

	class Meta:
		model= Cuenta

		fields=[
			'idCuenta',
			'nombre',
			'fkCategoria',
			
					]
		labels = {
			'idCuenta':'Introduzca el codigo',
			'nombre': 'Nombre',
			'fkCategoria': 'Seleccione el tipo de categoria',
			
		}
		widgets= {
			'idCuenta': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'fkCategoria': forms.Select(attrs={'class':'form-control'}),
			
		}




RegistroDebe=Cuenta.objects.all()
RegistroHaber=Cuenta.objects.all()

class guardarTransaccion(forms.Form):
	
	fkRegistroDebe = forms.ModelMultipleChoiceField(RegistroDebe, label="Seleccionar cuenta debe", required=True)
	fkRegistroHaber = forms.ModelMultipleChoiceField(RegistroHaber, label="Seleccionar cuenta haber", required=True)
	monto=forms.DecimalField(max_digits=15, decimal_places=2)
	