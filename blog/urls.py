from django.urls import path 
from . import views 



urlpatterns = [
    path('', views.index, name='index'),
    path('inicio', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('getResponse', views.getResponse, name='getResponse'),
    path('obtenerinfo', views.AllInfo, name='obtenerinfo'),
    path('modal', views.modal, name='modal'),
    path('registrar/usuarios', views.registrarUsuarios, name='registrarUsarios'),
    path('contacted', views.AllInfoContacted, name='contacted'),
    path('info/<int:info_id>/complete', views.contacted, name='info_complete'),
    path('info/<int:info_id>/delete', views.eliminar, name='info_delete'),
    path('logout/', views.salir, name='logout'),
    path('login/', views.signin, name='login'),
  #  path('viewAdmin', views.viewAdmin, name='viewAdmin'),
    path('create/info/', views.create_info, name='create/info'),

]