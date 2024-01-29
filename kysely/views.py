from django.shortcuts import render
from django.http import HttpResponse


def indeksi(request):
    return HttpResponse("Hyppää voltti! olet kysely-apin index-sivulla!.")

