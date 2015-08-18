import datetime

from django.db import models
from django.utils import timezone

class Solvers(models.Model):
    Username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    fechaRegistro = models.DateTimeField('fecha de creacion')
    Email = models.EmailField(max_length=70)
    Name = models.CharField(max_length=200)
    Age = models.IntegerField(default=0)

    dato3 = 'Sheila Ricalde'
    def __str__(self):
    	return self.Username
class Skill(models.Model):
    username = models.ForeignKey(Solvers)
    skill = models.CharField(max_length=200)
    def __str__(self):
    	return self.skill