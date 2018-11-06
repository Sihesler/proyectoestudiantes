from django.conf.urls import url
from . import views
from estudiantes.views import index

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^$', views.index, name='index'),

]
