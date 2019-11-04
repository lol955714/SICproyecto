from __future__ import unicode_literals
from __future__ import absolute_import
from django.conf.urls import url
from apps.informesContables.views import *
from django.contrib.auth.views import LogoutView
app_name='informes'
urlpatterns=[
url(r'^indexInformes/', indexin,name="indexinf"),
url(r'^balancecomp/(?P<ini>\w+)/(?P<fin>\w+)', comprobacion,name="balCo"),
url(r'^balancegener/', general,name="balG"),
url(r'^cambiospatrimonio/', patrimonio,name="CambPa"),
url(r'^estadresultados/', resultado,name="res"),
url(r'^librodiario/', librodia,name="dia"),
]