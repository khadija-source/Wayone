from django.shortcuts import render
from .models import Trajet
from django.contrib.auth import login
from .forms import InscriptionForm
from django.shortcuts import render, redirect
from .models import Trajet, Profil

def liste_trajets(request):
    trajets = Trajet.objects.all().order_by('-date_creation')
    return render(request, 'trajets/liste_trajets.html', {'trajets': trajets})

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profil.objects.create(
                user=user,
                role=form.cleaned_data['role'],
                telephone=form.cleaned_data['telephone']
            )
            login(request, user)
            return redirect('liste_trajets')
    else:
        form = InscriptionForm()
    return render(request, 'trajets/inscription.html', {'form': form})