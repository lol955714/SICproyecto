from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.registroCuentas.forms import CuentaForm
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
