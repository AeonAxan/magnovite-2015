from django.db import models

from app.main.models import Profile

class Invoice(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    profile = models.ForeignKey(Profile)

    invoice_type = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=4, decimal_places=2)
