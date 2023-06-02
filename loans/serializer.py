from rest_framework import serializers
from borrower.models import Borrower
from investor.models import Investor
from .models import LoanRequest


class LoanSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = ['id','borrower','investor','annual_interest_rate','loan_amount',
                  'loan_total_amount','loan_period','status','start_date',
                  'end_date']

class LoanBorrowerSubmitRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = ['id','borrower','loan_amount','loan_period']

class LoanInvestorSubmitRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = ['id','investor','annual_interest_rate',"loan_amount",'start_date','end_date']

    # def update(self, instance, validated_data):
    #     instance.loan_total_amount = (instance.loan_amount * validated_data.get("loan_amount")) + instance.loan_amount + 3
    #     instance.save()
    #     return  instance
