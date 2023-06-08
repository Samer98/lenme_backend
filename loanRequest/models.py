from django.db import models
from investor.models import Investor
from borrower.models import Borrower

class LoanRequest(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.PROTECT)
    loan_amount = models.IntegerField()
    loan_period = models.IntegerField()
    status_choices = (
        ('Pending', 'Pending'),
        ('Offered', 'Offered'), # got investorOffer from any investor
        ('Funded', 'Funded'),
    )
    status = models.CharField(choices=status_choices, default='Pending', max_length=10,editable=False)


    class Meta:
        db_table = "Loan_Request"

