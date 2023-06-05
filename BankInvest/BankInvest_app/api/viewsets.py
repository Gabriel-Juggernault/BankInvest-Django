from rest_framework import viewsets
from BankInvest_app.api import serializers 
from BankInvest_app import models

class Viewseter_Cliente(viewsets.ModelViewSet):
    serializer_class = serializers.Serializer_Cliente
    queryset = models.Cliente.objects.all()
    
class Viewseter_Transacoes(viewsets.ModelViewSet):
    serializer_class = serializers.Serializer_Transacoes
    queryset = models.Transacoes.objects.all()
    
