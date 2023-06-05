
from django.db import models
from uuid import uuid4

class Cliente(models.Model):
    id_cliente = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.TextField(null=False)
    sobreNome = models.TextField(null=False)
    cpf = models.CharField(max_length=11, null=False)
    email = models.TextField(null= False )
    senha = models.CharField(max_length=12, null=False)
    saldo = models.FloatField(default=0)
    
    def __str__(self) -> str:
        return self.nome
    
class Transacoes(models.Model):
    id_transacoes = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.TextField(null=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateTimeField(auto_now=True)
    
    

    
    
    