from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import LoanSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import LoanRequest, InvestorOffer
from .serializer import *
from installment.serializer import *
from investor.serializer import *
from investor.models import Investor
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin
import datetime
from dateutil.relativedelta import relativedelta


# Create your views here.

@api_view(["POST"])
def accept_offer(request):
    if request.method == "POST":
        investor_offer = InvestorOffer.objects.get(id=request.data['investor_offer_id'])
        loan_request = LoanRequest.objects.get(id=investor_offer.loan_request_id)
        investor_information = Investor.objects.get(id = investor_offer.investor_id)
        investor_balance = investor_information.balance
        if investor_balance < loan_request.loan_amount:
            return Response("There is no sufficient balance ")
        try:
            Loan.objects.get(loan_request_id=investor_offer.loan_request_id)
            return Response("This Loan Request already funded")
        except Loan.DoesNotExist:
            pass

        total_amount = (loan_request.loan_amount * (investor_offer.annual_interest_rate / 10)) + 3
        start_date = datetime.datetime.now()
        end_date = datetime.datetime.now() + relativedelta(months=investor_offer.loan_period)
        loan = {
            "total_amount": total_amount,
            "start_date": start_date,
            "end_date": end_date,
            "status": "Funded",
            "investor_offer_id": request.data['borrower_id'],
            "loan_request_id": investor_offer.loan_request_id
        }
        serializer = LoanSerializer(data=loan)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # print(serializer)
        for installment in range(investor_offer.loan_period):
            installments = {
                "due_date": datetime.datetime.now() + relativedelta(months=installment),
                "amount": total_amount / investor_offer.loan_period,
                "paid": False,
                "loan_id": serializer.data['id']
            }
            print(installments)
            installment_serializer = InstallmentSerializer(data=installments)
            installment_serializer.is_valid(raise_exception=True)
            installment_serializer.save()
        investor = {
            'name': investor_information.name,
            "balance":investor_information.balance - loan_request.loan_amount
        }
        investor_serializer = InvestorSerializer(data=investor)
        investor_serializer.is_valid(raise_exception=True)
        investor_serializer.save()
        return Response(serializer.data)


class LoanViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
