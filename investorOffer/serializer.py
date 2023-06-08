from rest_framework import serializers
from .models import InvestorOffer
from investorOffer.models import InvestorOffer



class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorOffer
        fields = ['id','annual_interest_rate','loan_period','investor_id','status','loan_request_id']

