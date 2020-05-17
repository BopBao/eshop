from django.contrib import admin
from .models import Lead, App, Accounting, Payment, Recommended, Addon, MonthlyVolume, BillingCycle
# Register your models here.

admin.site.register(Lead)
admin.site.register(App)
admin.site.register(Accounting)
admin.site.register(Payment)
admin.site.register(Recommended)
admin.site.register(Addon)
admin.site.register(MonthlyVolume)
admin.site.register(BillingCycle)
