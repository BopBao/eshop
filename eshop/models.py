from django.db import models

# Create your models here.


class Addon(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BillingCycle(models.Model):
   name= models.CharField(max_length=255)
   number_of_weeks_in_cycle = models.IntegerField(default=0)
   discount_percent = models.IntegerField(default=0)

   def __str__(self):
       return self.name  

class MonthlyVolume(models.Model):
    name = models.CharField(max_length = 255)
    volume = models.IntegerField(default=0)
    discount_percent = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Payment(models.Model):
    name=models.CharField(max_length=255)
    image = models.ImageField(upload_to='payment', null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name

class Accounting(models.Model):
    name=models.CharField(max_length=255)
    payments = models.ManyToManyField(Payment)
    image = models.ImageField(upload_to='accounting', null=True)

    def __str__(self):
        return self.name

class App(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='apps', null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    description = models.TextField(default="")
    accounting = models.ManyToManyField(Accounting, null=True)

    def __str__(self):
        return self.name

class Recommended(models.Model):
    name=models.CharField(max_length=255)
    models = models.ForeignKey(App, on_delete=models.CASCADE)

class Lead(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, default="")
    role = models.CharField(max_length=255, default="")
    company_id = models.CharField(max_length=255, default="")
    addons = models.ForeignKey(Addon, on_delete=models.SET_NULL, null=True)
    monthly_volume = models.ForeignKey(MonthlyVolume, on_delete=models.SET_NULL, null=True)
    billing_cycle = models.ForeignKey(BillingCycle, on_delete=models.SET_NULL, null=True)
    accounting = models.ForeignKey(Accounting, on_delete=models.SET_NULL, null=True)
    app_type = models.ForeignKey(App, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
class AboutUs(models.Model):
    description=models.TextField(default="")
    image = models.ImageField(upload_to='about_us', null=True)

class Features(models.Model):
    title=models.CharField(max_length=255, default="")
    description=models.TextField(default="")
    icon=models.ImageField(upload_to='features', null=True)

    def __str__(self):
        return self.title

class CalculateSection(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")

    def __str__(self):
        return self.title