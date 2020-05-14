from django.contrib import admin
from .models import Lead, LeadItem, Inventory
# Register your models here.

admin.site.register(Lead)
admin.site.register(LeadItem)
admin.site.register(Inventory)
