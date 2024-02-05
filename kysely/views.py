from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Kysymys


def indeksi(request):
    kysymyslista = Kysymys.objects.order_by("-julkaisupvm")[:2]
    context = {
        "kysymykset": kysymyslista,
    }
    return render(request, "kysely/indeksi.html", context)


def näytä(request, kysymys_id):
    kysymys = get_object_or_404(Kysymys, pk=kysymys_id )

    return render(request, "polls/detail.html", {"kysymys": kysymys})


def tulokset(request, kysymys_id):
    return HttpResponse(f"Katsot kysymyksen {kysymys_id} tuloksia")


def äänestä(request, kysymys_id):
    return HttpResponse(f"Olet äänestämässä kysymykseen {kysymys_id}")