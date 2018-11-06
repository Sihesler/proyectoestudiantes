from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^$', views.index, name='index'),
    url(r'^listar/estudiante/$', views.estudiante_list, name='estudiante_list'),
    url(r'^listar_curso$', views.curso_list, name='curso_list'),
    url(r'^nuevo$', views.curso_nuevo, name='curso_nuevo'),
    url(r'^nuevo_estudiante$', views.estudiante_nuevo, name='estudiante_nuevo'),
    url(r'^estudiante/(?P<pk>[0-9]+)/$', views.estudiante_detalle, name='estudiante_detalle'),
    url(r'^curso/(?P<pk>[0-9]+)/$', views.curso_detalle, name='curso_detalle'),
    url(r'^estudiante/(?P<pk>\d+)/remove/$', views.estudiante_remove, name='estudiante_remove'),
    url(r'^curso/(?P<pk>\d+)/remove/$', views.curso_remove, name='curso_remove'),

    #url(r'^detalle$', views.curso_detalle, name='curso_detalle'),
    #url(r'^listar$', views.curso_list, name='curso_list'),
]
