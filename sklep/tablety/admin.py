from django.contrib import admin

from .models import Dostawcy, Produkty, Oceny
# Register your models here.



@admin.register(Dostawcy)
class DostawcyAdmin(admin.ModelAdmin):
    pass

@admin.register(Produkty)
class ProduktyAdmin(admin.ModelAdmin):
    list_filter = ["producent"]
    list_display = ["producent", "model"]

@admin.register(Oceny)
class OcenyAdmin(admin.ModelAdmin):
    list_display = ["ocena", "produkt"]