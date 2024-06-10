from django.urls import path
from tablety.views import wszystkie_produkty

urlpatterns = [
    path('test', wszystkie_produkty)
]