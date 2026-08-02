from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trajet, Profil


class TrajetForm(forms.ModelForm):
    class Meta:
        model = Trajet
        fields = ['point_depart', 'point_arrivee', 'date_depart', 'places_disponibles', 'prix']


class InscriptionForm(UserCreationForm):
    role = forms.ChoiceField(choices=Profil.ROLE_CHOICES, label="Je suis un")
    telephone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'telephone']