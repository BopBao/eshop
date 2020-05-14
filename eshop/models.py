from django.db import models

# Create your models here.


class Inventory(models.Model):
    item = models.CharField(max_length=255)

    def __str__(self):
        return self.item


class Lead(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class LeadItem(models.Model):
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)