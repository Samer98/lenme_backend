from django.db import models
from investor.models import Investor
from borrower.models import Borrower

class LoanRequest(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.PROTECT)
    investor = models.ForeignKey(Investor, on_delete=models.PROTECT,null=True)
    annual_interest_rate = models.IntegerField(null=True)
    loan_amount = models.IntegerField(null=True)
    loan_total_amount = models.DecimalField(max_digits=8, decimal_places=2,editable=False,null=True)
    loan_period = models.IntegerField()
    status_choices = (
        ('Pending', 'Pending'),
        ('Offered', 'Offered'),
        ('Funded', 'Funded'),
        ('Completed', 'Completed'),
        ('Delayed', 'Delayed'),
    )
    status = models.CharField(choices=status_choices, default='Pending', max_length=10,editable=False)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    class Meta:
        db_table = "LoanRequest"

