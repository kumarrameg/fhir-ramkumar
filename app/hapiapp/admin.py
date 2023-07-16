from django.contrib import admin
from .models import Patient,Encounter,Observation


admin.site.register(Patient)
admin.site.register(Encounter)
admin.site.register(Observation)



