from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.inventario.forms import InventarioForm
from apps.informesContables.models import Producto
from django.urls import reverse_lazy

def inventario_view(request):
	if request.method == 'POST':
		form = InventarioForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('inventario_listar')
	else: 
			form = InventarioForm()
			return render(request, 'inventario/inventario_form.html', {'form':form})

def inventario_list(request):
	listinventario = Producto.objects.all().order_by('codigo')
	contexto = {'listinventario':listinventario} 
	return render(request, 'inventario/inventario_list.html', contexto)

def inventario_edit(request, id_producto):
	producto = Producto.objects.get(codigo=id_producto)
	if request.method == 'GET':
		form = InventarioForm(instance=producto)
	else:
		form = InventarioForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
			return redirect('inventario_listar')
	return render(request, 'inventario/inventario_form.html', {'form':form})


def inventario_delete(request, id_producto):
	producto = Producto.objects.get(codigo=id_producto)
	if request.method == 'POST':
		producto.delete()
		return redirect('inventario_listar')
	return render(request, 'inventario/inventario_delete.html', {'producto':producto})