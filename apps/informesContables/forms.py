from django import forms
fechas=[
		(1,'Enero'),
		(2,'Febrero'),
		(3,'Marzo'),
		(4,'Abril'),
		(5,'Mayo'),
		(6,'Junio'),
		(7,'Julio'),
		(8,'Agosto'),
		(9,'Setiembre'),
		(10,'Octubre'),
		(11,'Noviembre'),
		(12,'Diciembre'),
		]
informes=[
		(1,'Balance de Comprobación'),
		(2,'Balance General'),
		(3,'Estado de cambios en el patrimonio'),
		(4,'Estado de resultados'),
		(5,'Libro Diario'),
		]

class eleccion(forms.Form):
	inicio=forms.TypedChoiceField(choices=fechas,coerce=int,required=True, label="Seleccione el mes de inicio")
	final=forms.TypedChoiceField(choices=fechas,coerce=int,required=True,label="Seleccione el mes final")
	informe=forms.ChoiceField(choices=informes, required=True,label="Seleccione el informe a generar")