from django.shortcuts             import render
from rest_framework               import status
from rest_framework.decorators    import api_view
from rest_framework.response      import Response
from rest_framework.parsers       import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models                  import Cliente
from .serializers                 import ClienteSerializer

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_clientes(request):
    if request.method == 'GET':
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)