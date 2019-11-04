from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.informesContables.models import *

@login_required
def indexin(request):
    return render(request, 'estadosF/indexEstado.html', {})

@login_required
def comprobacion(request,ini,fin):
    cuenta = Cuenta.objects.all()
    transaccion = Transaccion.objects.all()
    haber = RegistroHaber.objects.all()
    debe = RegistroDebe.objects.all()
    contexto = {'transacciones': transaccion, 'cuentas': cuenta, 'habers': haber, 'debes': debe, }
    return render(request, 'estadosF/balComp.html', contexto)

@login_required
def general(request):
    return render(request, 'estadosF/balGen.html', {})

@login_required
def patrimonio(request):
    return render(request, 'estadosF/estaPatri.html', {})

@login_required
def librodia(request):
    return render(request, 'estadosF/libroDiario.html', {})

@login_required
def resultado(request):
    return render(request, 'estadosF/estaRes.html', {})