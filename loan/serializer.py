from rest_framework import serializers
from .models import Loan
from investorOffer.models import InvestorOffer



class LoanSerializer(serializers.ModelSerializer):
    loan_request_id = serializers.IntegerField()
    investor_offer_id = serializers.IntegerField()

    class Meta:
        model = Loan
        fields = ['id','total_amount','start_date','end_date','status','investor_offer_id','loan_request_id']

