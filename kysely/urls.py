from django.urls import path

from . import views

urlpatterns = [
    # ex: /kyselyt/
     path("", views.indeksi, name="index"),
    # ex: /kyselyt/5/
    path("<int:question_id>/", views.yksityiskohdat, name="yksityiskohdat"),
    # ex: /kyselyt/5/tulokset/
    path("<int:question_id>/results/", views.tulokset, name="tulokset"),
    # ex: /kyselyt/5/äänestä/
    path("<int:question_id>/vote/", views.äänestä, name="äänestä"),
]