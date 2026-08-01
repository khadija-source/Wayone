from django.contrib import admin
from .models import Trajet , Reservation , Notification

admin.site.register(Trajet)
admin.site.register(Reservation)
admin.site.register(Notification)