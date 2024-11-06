from django.urls import path
from . import views

urlpatterns = [
    path('', views.kalkulator),
    path('conversi-panjang', views.panjang),
    path('conversi-suhu', views.suhu)
]
