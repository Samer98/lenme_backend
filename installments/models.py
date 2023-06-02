from django.db import models
from loans.models import LoanRequest

# Create your models here.
class Installments(models.Model):
    loan = models.ForeignKey(LoanRequest, on_delete=models.CASCADE)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid = models.BooleanField(default=False)

    class Meta:
        db_table = "installments"
