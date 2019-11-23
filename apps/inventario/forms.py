from django import forms

from apps.informesContables.models import Producto

class InventarioForm(forms.ModelForm):

	class Meta:
		model= Producto

		fields=[
			'fkCategoría',
			'codigo',
			'nombre',
			'existencia',
			
					]
		labels = {
			'fkCategoría':'Seleccione la categoria',
			'codigo': 'Escriba el codigo',
			'nombre': 'Escriba el nombre del producto',
			'existencia': 'Escriba la existencia ',
			
		}
		widgets= {
			'fkCategoría': forms.Select(attrs={'class':'form-control'}),
			'codigo': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'existencia': forms.TextInput(attrs={'class':'form-control'}),
			
		}