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

class eleccion(forms.Form):
	inicio=forms.ChoiceField(choices=fechas,required=True, label="seleccione el inicio")
	final=forms.ChoiceField(choices=fechas,required=True,label="ingrese la fecha de finalización")