from django.db import models
from loanRequest.models import LoanRequest
from investorOffer.models import InvestorOffer


# Create your models here.

class Loan(models.Model):
    loan_request = models.ForeignKey(LoanRequest, on_delete=models.PROTECT)
    investor_offer = models.ForeignKey(InvestorOffer, on_delete=models.PROTECT)
    total_amount = models.PositiveSmallIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status_choices = (
        ('Funded', 'Funded'),  # On going the borrower got the money
        ('Delayed', 'Delayed'),
        ('Completed', 'Completed'),

    )
    status = models.CharField(choices=status_choices, default='Pending', max_length=10, editable=False)

    class Meta:
        db_table = "loan"
