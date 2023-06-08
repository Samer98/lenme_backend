from django.db import models
from loanRequest.models import LoanRequest
from investor.models import Investor

# Create your models here.

class InvestorOffer(models.Model):
    loan_request = models.ForeignKey(LoanRequest,on_delete=models.PROTECT)
    investor = models.ForeignKey(Investor,on_delete=models.PROTECT)
    annual_interest_rate = models.PositiveSmallIntegerField()
    loan_period = models.IntegerField() #In month

    status_choices = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),

    )
    status = models.CharField(choices=status_choices, default='Pending', max_length=10,editable=False)

    class Meta:
        db_table = "Investor_Offer"
