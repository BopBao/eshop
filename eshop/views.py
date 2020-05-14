from django.shortcuts import render
from django.views.generic import CreateView
from .models import Lead
from .forms import LeadForm
from .models import Inventory

# Create your views here.

def lead_page(request):
    form = LeadForm()
    return render(request, 'eshop/lead_form.html', {'form': form, 'inventory': Inventory.objects.all()})

