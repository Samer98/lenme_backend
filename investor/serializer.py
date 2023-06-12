from rest_framework import serializers
from investor.models import Investor

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ['id', 'name', 'balance']
