from django.shortcuts import render
from django.views.generic import CreateView
from .models import Lead, App, Accounting, Payment, Recommended, MonthlyVolume, BillingCycle, Features, AboutUs
from .forms import LeadForm, SalesForm
from .models import App, CalculateSection
import logging
# Create your views here.
logger = logging.getLogger(__name__)

def lead_page(request):
    form = LeadForm()
    salesform = SalesForm()

    if request.method == 'POST':
        submit_form = LeadForm(data=request.POST)
        if submit_form.is_valid():
            name=submit_form.cleaned_data['name']
            company_name=submit_form.cleaned_data['company_name']
            company_id=submit_form.cleaned_data['company_id']
            role=submit_form.cleaned_data['role']
            phone_number = submit_form.cleaned_data['phone_number']
            email = submit_form.cleaned_data['email']
            addons = submit_form.cleaned_data['addons']
            monthly_volume = submit_form.cleaned_data['monthly_volume']
            billing_cycle = submit_form.cleaned_data['billing_cycle']
            accounting = submit_form.cleaned_data['accounting']
            app_type = submit_form.cleaned_data['app_type']
            payment = submit_form.cleaned_data['payment']

            lead = Lead()
            lead.name = name
            lead.company_name = company_name
            lead.company_id = company_id
            lead.role = role
            lead.phone_number = phone_number
            lead.email = email
            lead.addons = addons
            lead.monthly_volume = monthly_volume
            lead.billing_cycle = billing_cycle
            lead.accounting = accounting
            lead.app_type = app_type
            lead.payment = payment

            lead.save()
   
    return render(request, 'eshop/lead_form.html', 
    {'form': form, 
    'salesform': salesform,
    'apps': App.objects.all(),
    'recommendeds': Recommended.objects.all(), 
    'accountings': Accounting.objects.all(), 
    'payments': Payment.objects.all(),
    'volume': MonthlyVolume.objects.all(),
    'cycle': BillingCycle.objects.all(),
    'about': AboutUs.objects.all(),
    'features': Features.objects.all(),
    'calculate': CalculateSection.objects.all()

     })