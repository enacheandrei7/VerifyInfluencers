from django.contrib import admin
from .models import Influencer, HealthClaim

# Register your models here.
admin.site.register(Influencer)
admin.site.register(HealthClaim)