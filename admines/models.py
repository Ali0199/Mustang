from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Karobka(models.Model):
    nomi = models.CharField(max_length=50)
    soni=models.IntegerField()
    kg=models.FloatField(max_length=5)
    narxi=models.FloatField(max_length=10)
    def __str__(self):
        return self.nomi

class Idish(models.Model):
    nomi = models.CharField(max_length=50)
    soni=models.IntegerField()
    kg=models.FloatField(max_length=4)
    narxi=models.FloatField(max_length=10)
    def __str__(self):
        return self.nomi

class Etiketika(models.Model):
    nomi = models.CharField(max_length=50)
    soni=models.IntegerField()
    kg=models.FloatField(max_length=5)
    narxi=models.FloatField(max_length=10)

    def __str__(self):
        return self.nomi

class Kraska(models.Model):
    nomi = models.CharField(max_length=50)
    karobka=models.ForeignKey(Karobka, on_delete=models.CASCADE)
    ksoni=models.IntegerField()
    etiketika=models.ForeignKey(Etiketika, on_delete=models.CASCADE)
    idish=models.ForeignKey(Idish, on_delete=models.CASCADE)
    kg=models.FloatField(max_length=5)  
    soni=models.IntegerField()
    narxi=models.FloatField(max_length=10)
    def __str__(self):
        return self.nomi

class Kirim(models.Model):
    nomi = models.CharField(max_length=50)
    turi = models.CharField(max_length=50)
    soni=models.IntegerField()
    narxi=models.FloatField(max_length=10)

class Chiqim(models.Model):
    nomi = models.CharField(max_length=50)
    turi = models.CharField(max_length=50)
    soni=models.IntegerField()
    narxi=models.FloatField(max_length=10)




