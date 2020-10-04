from django.contrib import admin

from jobs.models import jobOffer, Company

# Register your models here.

admin.site.register(jobOffer)
admin.site.register(Company)
