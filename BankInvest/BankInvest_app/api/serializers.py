from rest_framework import serializers
from BankInvest_app import models


class Serializer_Cliente(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = "__all__"
        
class Serializer_Transacoes(serializers.ModelSerializer):
    class Meta:
        model = models.Transacoes
        fields = "__all__"
        
  

        