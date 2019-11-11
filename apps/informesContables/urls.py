from __future__ import unicode_literals
from __future__ import absolute_import
from django.conf.urls import url
from apps.informesContables.views import *
from django.contrib.auth.views import LogoutView
app_name='informes'
urlpatterns=[
url(r'^principal/', inicio,name="indexp"),
url(r'^indexInformes/', indexin,name="indexinf"),
url(r'^balancecomp/(?P<ini>\w+)/(?P<fin>\w+)', comprobacion,name="balCo"),
url(r'^balancegener/(?P<ini>\w+)/(?P<fin>\w+)', general,name="balG"),
url(r'^cambiospatrimonio/(?P<ini>\w+)/(?P<fin>\w+)', patrimonio,name="CambPa"),
url(r'^estadresultados/(?P<ini>\w+)/(?P<fin>\w+)', resultado,name="res"),
url(r'^librodiario/(?P<ini>\w+)/(?P<fin>\w+)', librodia,name="dia"),
]