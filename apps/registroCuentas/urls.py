from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.registroCuentas.views import cuenta_view, cuenta_list, cuenta_edit, cuenta_delete, crearTransaccion
from apps.registroCuentas.views import transaccion_list, transaccion_delete, editTransaccion

urlpatterns = [
    #url(r'^$', index, name='index_principal'),
     url(r'^nuevo$', cuenta_view, name='cuenta_crear'),
  	 url(r'^listar$', cuenta_list, name='cuenta_listar'),
  	 url(r'^editar/(?P<id_cuenta>\d+)/$', cuenta_edit, name='cuenta_editar'),
  	 url(r'^eliminar/(?P<id_cuenta>\d+)/$', cuenta_delete, name='cuenta_eliminar'),
  	

  	 url(r'^listaTransaccion$', transaccion_list, name='transaccion_listar'),
  	 url(r'^transaccion/eliminar/(?P<id>\d+)/$', transaccion_delete, name='transaccion_eliminar'),
  	 url(r'^nuevaTransaccion$', crearTransaccion, name='transaccion_crear'),

  	 

]
