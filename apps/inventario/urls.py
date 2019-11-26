from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.inventario.views import inventario_view, inventario_list, inventario_edit, inventario_delete, index

urlpatterns = [
		url(r'^$', index, name='index_inventario'),
 		url(r'^nuevo$', inventario_view, name='inventario_crear'),
  	 	url(r'^listar$', inventario_list, name='inventario_listar'),
  	 	url(r'^editar/(?P<id_producto>\d+)/$', inventario_edit, name='inventario_editar'),
     	url(r'^eliminar/(?P<id_producto>\d+)/$', inventario_delete, name='inventario_eliminar'),
]