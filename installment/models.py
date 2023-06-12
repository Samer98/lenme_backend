from django.db import models
from loan.models import Loan

# Create your models here.
class Installment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    amount = models.FloatField()
    paid = models.BooleanField(default=False)

    class Meta:
        db_table = "installment"
