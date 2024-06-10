from django.forms import ModelForm
from .models import Produkty, Dostawcy, Oceny

class ProduktyForm(ModelForm):
    class Meta:
        model = Produkty
        fields = ["producent", "model", "opis", "liczba_sztuk", "cena", "zdjecie_produktu", "dostawca"]

class OcenyForm(ModelForm):
    class Meta:
        model = Oceny
        fields = ["ocena", "recenzja"]
