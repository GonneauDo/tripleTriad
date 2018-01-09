from django.db import models
from django.utils import timezone


class Carte(models.Model):
    Nom = models.CharField(max_length=80)
    haut = models.BigIntegerField()
    bas = models.BigIntegerField()
    droite = models.BigIntegerField()
    gauche = models.BigIntegerField()

    def __int__(self):
        return self.haut

    def __int__(self):
        return self.bas

    def __int__(self):
        return self.droite

    def __int__(self):
        return self.gauche
