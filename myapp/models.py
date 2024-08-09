from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_jury = models.BooleanField('Is jury', default=False)
    is_candidat = models.BooleanField('Is Candidatd', default=False)

class Jury(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    note = models.IntegerField(default=0)


    def __str__ (self):
        return(f"{self.first_name} {self.last_name} {self.username} {self.email} {self.phone}")

class Travail(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    num_inscription = models.CharField(max_length=20)
    categorie = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    jurys = models.ManyToManyField(Jury, related_name='travail', blank=True)


class Candidature(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    matricule = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    num_cin = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    direction = models.CharField(max_length=10)
    travail = models.ForeignKey(Travail, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__ (self):
        return(f"{self.matricule} {self.first_name} {self.last_name} {self.email} {self.num_cin} {self.phone} {self.email}")

