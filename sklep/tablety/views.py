from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Produkty, Oceny, Dostawcy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ProduktyForm, OcenyForm


from django.contrib.auth import logout

def wyloguj(request):
    logout(request)
    return redirect('tablety')

def zaloguj(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(wszystkie_produkty)
    return render(request, 'registration/login.html')

def wszystkie_produkty(request):
    wszystkie = Produkty.objects.all()
    wszystkie_oceny = Oceny.objects.all()
    return render(request, 'Produkty.html', {"produkty": wszystkie, "oceny": wszystkie_oceny })

@login_required
def dodaj_produkt(request):
    form = ProduktyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_produkty)
    return render(request, 'Produkt_form.html', {"form" : form})


@login_required
def edytuj_produkt(request, id):
    produkt = get_object_or_404(Produkty, pk=id)
    oceny = Oceny.objects.filter(produkt=produkt)

    form_produkt = ProduktyForm(request.POST or None, request.FILES or None, instance=produkt)
    form_ocena = OcenyForm(request.POST or None, request.FILES or None, instance=produkt)

    if request.method == "POST":
        form_ocena = OcenyForm(request.POST)
        if form_ocena.is_valid():
            ocena = form_ocena.save(commit=False)
            ocena.film = produkt
            ocena.save()

    if form_produkt.is_valid():
        produkt = form_produkt.save(commit=False)
        produkt.save()
        return redirect(wszystkie_produkty)
    return render(request, 'Produkt_form.html',
                  {'form': form_produkt, 'form_ocena': form_ocena, 'oceny': oceny,
                   'nowy': True})


@login_required
def usun_produkt(request, id):
    produkt = get_object_or_404(Produkty, pk=id)

    if request.method == "POST":
        produkt.delete()
        return redirect(wszystkie_produkty)
    return render(request, 'Potwierdz.html', {'produkt': produkt})

def ocen_produkt(request, id):
    produkt = get_object_or_404(Produkty, pk=id)
    form_ocena = OcenyForm(request.POST or None)
    if request.method == 'POST' and form_ocena.is_valid():
        ocena = form_ocena.save(commit=False)
        ocena.produkt = produkt
        ocena.save()
        return redirect(wszystkie_produkty)
    return render(request, 'ocen_produkt.html', {'form': form_ocena, 'produkt': produkt})