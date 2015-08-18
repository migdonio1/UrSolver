from django.forms import ModelForm
from django import forms
from polls.models import Solvers,Skill

class Usuarioform(forms.Form):
    class Meta:
        model = Solvers