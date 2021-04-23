from django.db import models


class Auto(models.Model):
  SPZ = models.CharField(max_length=10)
  Typ = models.CharField(max_length=100)
  KM = models.IntegerField()
  STK = models.DateField()

class Zakaznik(models.Model):
  Jméno= models.CharField(max_length=30)
  Příjmení = models.CharField(max_length=30)
  ČísloŘP= models.CharField(max_length=15)
  Datum_narození = models.DateField()

class Vypujcka(models.Model):
  Začátek = models.DateTimeField()
  Konec = models.DateTimeField()
  Cena = models.IntegerField()

