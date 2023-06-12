from rest_framework import serializers
from investorOffer.models import InvestorOffer



class InvestorOfferSerializer(serializers.ModelSerializer):
    loan_request_id = serializers.IntegerField()
    investor_id = serializers.IntegerField()
    class Meta:
        model = InvestorOffer
        fields = ['id','annual_interest_rate','loan_period','investor_id','status','loan_request_id']

