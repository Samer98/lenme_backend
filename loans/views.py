from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import  LoanRequest
from .serializer import *
from rest_framework.viewsets import ModelViewSet , GenericViewSet
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin, CreateModelMixin, UpdateModelMixin


class LoanViewSet(RetrieveModelMixin,ListModelMixin,GenericViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanSerializers

@api_view(["POST"])
def submit_investor_request(request,id):
    if request.method == "POST":
        loan = LoanRequest.objects.get(id=id)
        serializer = LoanInvestorSubmitRequestSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        loan.objects.update(loan_total_amount = loan.loan_amount * serializer.data.annual_interest_rate)
        # loan.
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(["POST"])
def submit_borrower_request(request):
    if request.method == "POST":
        serializer = LoanBorrowerSubmitRequestSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
