from django.contrib import admin
from django.urls import path, include
from BankInvest_app.api import viewsets
from rest_framework import routers

rota = routers.DefaultRouter()
rota.register(r"Rota_Cliente", viewsets.Viewseter_Cliente)
rota.register(r"Rota_Transacoes", viewsets.Viewseter_Transacoes)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rota.urls))
]
