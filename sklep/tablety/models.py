from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Dostawcy(models.Model):
    nazwa_dostawcy = models.CharField(max_length=64)

    def __str__(self):
        return self.nazwa_dostawcy

class Produkty(models.Model):
    producent = models.CharField(max_length=64, blank=False)
    model = models.CharField(max_length=64, blank=False)
    opis = models.TextField(default="")
    liczba_sztuk = models.PositiveSmallIntegerField(default=10)
    cena = models.DecimalField(max_digits=6, decimal_places=2, blank=False, unique=True)
    zdjecie_produktu = models.ImageField(upload_to="zdjecia", null=True, blank=True)
    dostawca = models.ForeignKey(Dostawcy, on_delete=models.CASCADE)

    def __str__(self):
        return self.tekst()

    def tekst(self):
        return "{} ({})".format(self.producent, self.model)

class Oceny(models.Model):
    ocena = models.IntegerField(default=5, blank=False)
    recenzja = models.TextField(default="", blank=False)
    produkt = models.ForeignKey(Produkty, on_delete=models.CASCADE, related_name='oceny')

    def __str__(self):
        return str(self.ocena)