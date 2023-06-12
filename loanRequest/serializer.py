from rest_framework import serializers
from borrower.models import Borrower
from investor.models import Investor
from .models import LoanRequest


class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = ['id','borrower','loan_amount',
                  'loan_period','status']

