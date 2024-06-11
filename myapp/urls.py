from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('registro/', views.register, name="registro"),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos_list, name='productos'),
    path('prodAdmin/', views.productos_list_admin, name='prodadmin'),
    path('prodAdmin/agregar/', views.agregar_producto, name='agregar_producto'),
    path('prodAdmin/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('prodAdmin/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]
