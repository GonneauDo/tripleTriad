from django.db import models
from django.utils import timezone


class Carte(models.Model):
    Nom = models.ForeignKey('auth.User')
    valueH = models.BigIntegerField()
    valueD = models.BigIntegerField()
    valueB = models.BigIntegerField()
    valueG = models.BigIntegerField()

    def __int__(self):
        return self.valueH

    def __int__(self):
        return self.valueD

    def __int__(self):
        return self.valueB

    def __int__(self):
        return self.valueG
