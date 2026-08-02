from django.contrib import admin
from .models import Trajet , Reservation , Notification , Profil

admin.site.register(Trajet)
admin.site.register(Reservation)
admin.site.register(Notification)
admin.site.register(Profil)