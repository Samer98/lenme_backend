from rest_framework import serializers
from .models import Installment


class InstallmentSerializer(serializers.ModelSerializer):
    loan_id = serializers.IntegerField()

    class Meta:
        model = Installment
        fields = ['id','due_date','amount','paid','loan_id']
