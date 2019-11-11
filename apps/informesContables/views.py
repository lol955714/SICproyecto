from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from apps.informesContables.models import *
from apps.informesContables.forms import *

@login_required
def indexin(request):
    if request.method=='POST':
        form=eleccion(request.POST)
        if form.is_valid(): 
            form_data=form.cleaned_data
            informe=form_data.get("informe")
            if informe=='1':
                direccion='/informes/balancecomp/'+str(form_data.get("inicio"))+("/")+str(form_data.get("final"))
            elif informe=='2':
                direccion='/informes/balancegener/'+str(form_data.get("inicio"))+("/")+str(form_data.get("final"))
            elif informe=='3':
                direccion='/informes/cambiospatrimonio/'+str(form_data.get("inicio"))+("/")+str(form_data.get("final"))
            elif informe=='4':
                direccion='/informes/estadresultados/'+str(form_data.get("inicio"))+("/")+str(form_data.get("final"))
            elif informe=='5':
                direccion='/informes/librodiario/'+str(form_data.get("inicio"))+("/")+str(form_data.get("final"))
        return HttpResponseRedirect(direccion)
    else:
        form=eleccion()
    return render(request, 'estadosF/indexEstado.html', {'form':form})

@login_required
def comprobacion(request,ini,fin):
    cuenta = Cuenta.objects.all()
    transaccion = Transaccion.objects.all()
    haber = RegistroHaber.objects.all()
    debe = RegistroDebe.objects.all()
    contexto = {'transacciones': transaccion, 'cuentas': cuenta, 'habers': haber, 'debes': debe,'Vinis': int(ini), 'Vfins':int(fin),}
    return render(request, 'estadosF/balComp.html', contexto)

@login_required
def inicio(request):
    return render(request, 'estadosF/index.html', {})

@login_required
def general(request,ini,fin):
    cuenta = Cuenta.objects.all()
    transaccion = Transaccion.objects.all()
    haber = RegistroHaber.objects.all()
    debe = RegistroDebe.objects.all()
    contexto = {'transacciones': transaccion, 'cuentas': cuenta, 'habers': haber, 'debes': debe, 'Vinis': int(ini), 'Vfins': int(fin), }
    return render(request, 'estadosF/balGen.html', contexto)

@login_required
def patrimonio(request,ini,fin):
    cuenta = Cuenta.objects.all()
    transaccion = Transaccion.objects.all()
    haber = RegistroHaber.objects.all()
    debe = RegistroDebe.objects.all()
    contexto = {'transacciones': transaccion, 'cuentas': cuenta, 'habers': haber, 'debes': debe, 'Vinis': int(ini), 'Vfins': int(fin), }
    return render(request, 'estadosF/estaPatri.html', contexto)

@login_required
def librodia(request,ini,fin):
    cuenta = Cuenta.objects.all()
    transaccion = Transaccion.objects.all()
    haber = RegistroHaber.objects.all()
    debe = RegistroDebe.objects.all()
    contexto = {'transacciones': transaccion, 'cuentas': cuenta, 'habers': haber, 'debes': debe, 'Vinis': int(ini), 'Vfins': int(fin), }
    return render(request, 'estadosF/libroDiario.html', contexto)

@login_required
def resultado(request,ini,fin):
    cuenta = Cuenta.objects.all()
    transaccion = Transaccion.objects.all()
    haber = RegistroHaber.objects.all()
    debe = RegistroDebe.objects.all()
    contexto = {'transacciones': transaccion, 'cuentas': cuenta, 'habers': haber, 'debes': debe, 'Vinis': int(ini), 'Vfins': int(fin), }
    return render(request, 'estadosF/estaRes.html', contexto)