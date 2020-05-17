from django import forms
from .models import Lead, Accounting, App, Payment, Addon, BillingCycle, MonthlyVolume
from crispy_forms import helper, layout, bootstrap

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = helper.FormHelper(self)
        self.fields['addons'].widget = forms.HiddenInput()
        self.fields['monthly_volume'].widget = forms.HiddenInput()
        self.fields['billing_cycle'].widget = forms.HiddenInput()
        self.fields['payment'].widget = forms.HiddenInput()
        self.fields['app_type'].widget = forms.HiddenInput()
        self.fields['accounting'].widget = forms.HiddenInput()
        self.fields['addons'].required = False
        self.fields['monthly_volume'].required = False
        self.fields['billing_cycle'].required = False
        self.fields['payment'].required = False
        self.fields['app_type'].required = False
        self.fields['accounting'].required = False


class AccountingForm(forms.ModelForm):
    class Meta:
        model = Accounting
        fields = ('name',)

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('name',)

class AddonForm(forms.ModelForm):
    class Meta:
        model = Addon
        fields = ('name',)

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ('name',)

class VolumeForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ('name',)

class SalesForm(forms.Form):
    imports = forms.ModelChoiceField(queryset=App.objects.all(), required=False)
    account = forms.ModelChoiceField(queryset=Accounting.objects.all(), required=False)
    payments = forms.ModelChoiceField(queryset=Payment.objects.all(), required=False)
    addon = forms.ModelChoiceField(queryset=Addon.objects.all(), required=False)
    volume = forms.ModelChoiceField(queryset=MonthlyVolume.objects.all(), required=False)
    billing = forms.ModelChoiceField(queryset=BillingCycle.objects.all(), required=False)