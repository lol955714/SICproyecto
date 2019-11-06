from django import forms
fechas=[
		(1,'enero'),
		(2,'febrero'),
		(3,'marzo'),
		(4,'abril'),
		(5,'mayo'),
		(6,'junio'),
		(7,'julio'),
		(8,'agosto'),
		(9,'setiembre'),
		(10,'octubre'),
		(11,'nombiembre'),
		(12,'diciembre'),
		]
informes=[
		(1,'Balance de comprobación'),
		(2,'Balance general'),
		(3,'Cambios en el patrimonio'),
		(4,'estado de resultados'),
		(5,'Libro Diario'),
		]

class eleccion(forms.Form):
	inicio=forms.TypedChoiceField(choices=fechas,coerce=int,required=True, label="seleccione el inicio")
	final=forms.TypedChoiceField(choices=fechas,coerce=int,required=True,label="ingrese la fecha de finalización")
	informe=forms.ChoiceField(choices=informes, required=True,label="seleccione el informe a generar")