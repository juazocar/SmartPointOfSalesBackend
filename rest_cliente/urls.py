from django.urls import path
from rest_cliente.views import lista_clientes
from rest_cliente.viewsLogin import login

urlpatterns = [
    path('lista_clientes', lista_clientes, name="lista_clientes"),
    path('login', login, name="login"),
]