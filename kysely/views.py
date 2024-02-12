import datetime 

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Kysymys, Vaihtoehto



class ListaNäkymä(generic.ListView):
    template_name = "kysely/indeksi.html"
    context_object_name = "kysymykset"

    def get_queryset(self):
       
        nyt = timezone.now()
        
        kaikki_kysymykset = Kysymys.objects.all()
        
        ei_tulevaisuudessa = kaikki_kysymykset.filter(julkaisupvm__lte=nyt)
       
        järjestetyt_kysymykset = ei_tulevaisuudessa.order_by("-julkaisupvm")
            
            
        """Return the last five published questions."""
        return järjestetyt_kysymykset[:2]


class NäytäNäkymä(generic.DetailView):
    model = Kysymys
    template_name = "kysely/näytä.html"


class TuloksetNäkymä(generic.DetailView):
    model = Kysymys
    template_name = "kysely/tulokset.html"



''''
def indeksi(request):
    kysymyslista = Kysymys.objects.order_by("-julkaisupvm")[:2]
    context = {
        "kysymykset": kysymyslista,
    }
    return render(request, "kysely/indeksi.html", context)


def näytä(request, kysymys_id):
    kysym = get_object_or_404(Kysymys, pk=kysymys_id)
    return render(request, "kysely/näytä.html", {"kysymys": kysym})


def tulokset(request, kysymys_id):
    kysym = get_object_or_404(Kysymys, pk=kysymys_id)
    return render(request, "kysely/tulokset.html", {"kysymys": kysym})
'''

def äänestä(request, kysymys_id):
    kysym = get_object_or_404(Kysymys, pk=kysymys_id)
    try:
        valittu = kysym.vaihtoehto_set.get(pk=request.POST["valittu"])
    except (KeyError, Vaihtoehto.DoesNotExist):
        # Näytä kysymyslomake uudelleen
        return render(
            request,
            "kysely/näytä.html",
            {
                "kysymys": kysym,
                "virheviesti": "Et valinnut mitään vaihtoehtoa.",
            },
        )
    else:
        valittu.ääniä += 1
        valittu.save()
        osoite = reverse("kysely:tulokset", args=(kysym.id,))
        return HttpResponseRedirect(osoite)
