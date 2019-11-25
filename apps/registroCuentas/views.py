from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.registroCuentas.forms import CuentaForm, guardarTransaccion
from apps.informesContables.models import Cuenta, Transaccion, RegistroDebe, RegistroHaber
from django.urls import reverse_lazy


def cuenta_view(request):
	if request.method == 'POST':
		form = CuentaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('cuenta_listar')
	else: 
			form = CuentaForm()
			return render(request, 'cuenta/cuenta_form.html', {'form':form})

def cuenta_list(request):
	listcuenta = Cuenta.objects.all().order_by('id')
	contexto = {'listcuenta':listcuenta} 
	return render(request, 'cuenta/cuenta_list.html', contexto)

def cuenta_edit(request, id_cuenta):
	cuenta = Cuenta.objects.get(id=id_cuenta)
	if request.method == 'GET':
		form = CuentaForm(instance=cuenta)
	else:
		form = CuentaForm(request.POST, instance=cuenta)
		if form.is_valid():
			form.save()
			return redirect('cuenta_listar')
	return render(request, 'cuenta/cuenta_form.html', {'form':form})


def cuenta_delete(request, id_cuenta):
	cuenta = Cuenta.objects.get(id=id_cuenta)
	if request.method == 'POST':
		cuenta.delete()
		return redirect('cuenta_listar')
	return render(request, 'cuenta/cuenta_delete.html', {'cuenta':cuenta})


def transaccion_list(request):
	listaTran = Transaccion.objects.all().order_by('id')
	contexto = {'listaTran':listaTran} 
	return render(request, 'transaccion/transaccion_list.html', contexto)

def transaccion_delete(request, id):
	transaccion = Transaccion.objects.get(id=id)
	if request.method == 'POST':
		transaccion.delete()
		return redirect('transaccion_listar')
	return render(request, 'transaccion/transaccion_delete.html', {'transaccion':transaccion})


def crearTransaccion(request):
	if request.method=='POST':
		form=guardarTransaccion(request.POST)
		if form.is_valid():
			form_data=form.cleaned_data
			var1=form_data.get("fkRegistroHaber").get()
			var2=form_data.get("fkRegistroDebe").get()
			var3=form_data.get("monto")  
			transaccion=Transaccion()
			
			tabladebe=RegistroDebe()
			tabladebe.fkCuenta=var2
			tabladebe.monto=var3
			tabladebe.save()
			
			
			tablahaber=RegistroHaber()
			tablahaber.fkCuenta=var1
			tablahaber.monto=var3
			tablahaber.save()

			transaccion.fkRegistroDebe=tabladebe
			transaccion.fkRegistroHaber=tablahaber			

			transaccion.save()
			return redirect('transaccion_listar')

	else: 
		form=guardarTransaccion()
		contexto = {'form':form}
	return render(request, 'transaccion/crear_transaccion.html', contexto)



def editTransaccion(request, id):
	transaccion = Transaccion.objects.get(id=id)

	if request.method=='GET':
		form=guardarTransaccion(instance=transaccion)

	else: 
		form=guardarTransaccion(request.POST, instance=transaccion)
		if form.is_valid():

			form.save()
			return redirect('transaccion_listar')
	return render(request, 'transaccion/crear_transaccion.html', {'form':form})
