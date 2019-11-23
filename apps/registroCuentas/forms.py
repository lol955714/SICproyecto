from django import forms

from apps.informesContables.models import Cuenta

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