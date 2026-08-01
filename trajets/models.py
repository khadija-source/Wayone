from django.db import models
from django.contrib.auth.models import User

class Trajet(models.Model):
    conducteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trajets_proposes')
    point_depart = models.CharField(max_length=255)
    point_arrivee = models.CharField(max_length=255)
    date_depart = models.DateTimeField()
    places_disponibles = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.point_depart} → {self.point_arrivee} le {self.date_depart.strftime('%d/%m/%Y %H:%M')}"


class Reservation(models.Model):
    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'),
        ('CONFIRME', 'Confirmé'),
        ('ANNULE', 'Annulé'),
    ]

    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE, related_name='reservations')
    passager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='EN_ATTENTE')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passager.username} - {self.trajet} ({self.statut})"


class Notification(models.Model):
    TYPE_CHOICES = [
        ('CONFIRMATION', 'Confirmation'),
        ('ANNULATION', 'Annulation'),
    ]

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='notifications')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    message = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type} - {self.reservation}"