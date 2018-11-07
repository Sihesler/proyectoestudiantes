from django.conf.urls import url
from . import views

urlpatterns = [
    #URL de estudiantes
    url(r'^$', views.index, name='index'),
    url(r'^listar/estudiante/$', views.estudiante_list, name='estudiante_list'),
    url(r'^nuevo_estudiante$', views.estudiante_nuevo, name='estudiante_nuevo'),
    url(r'^estudiante/(?P<pk>[0-9]+)/$', views.estudiante_detalle, name='estudiante_detalle'),
    url(r'^estudiante/(?P<pk>\d+)/remove/$', views.estudiante_remove, name='estudiante_remove'),
    url(r'^estudiante/(?P<pk>[0-9]+)/editar/$', views.estudiante_editar, name='estudiante_editar'),

    #URL de Curso
    url(r'^listar_curso$', views.curso_list, name='curso_list'),
    url(r'^nuevo$', views.curso_nuevo, name='curso_nuevo'),
    url(r'^curso/(?P<pk>[0-9]+)/$', views.curso_detalle, name='curso_detalle'),
    url(r'^curso/(?P<pk>\d+)/remove/$', views.curso_remove, name='curso_remove'),
    url(r'^curso/(?P<pk>[0-9]+)/editar/$', views.curso_editar, name='curso_editar'),
]
