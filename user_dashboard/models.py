from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Dashboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    directorate = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    expenditure_type = models.CharField(max_length=200)
    ref_doc_1 = models.CharField(max_length=20)
    vendor_name = models.CharField(max_length=200)
    expenditure_amount = models.DecimalField(decimal_places=2, max_digits=10)
    payment_date = models.DateField()
