from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from investor.models import Investor
from .models import  InvestorOffer, LoanRequest
from .serializer import *
from rest_framework.viewsets import ModelViewSet , GenericViewSet
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin, CreateModelMixin, UpdateModelMixin


class InvestorOfferViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = InvestorOffer.objects.all()
    serializer_class = InvestorOfferSerializer

# Create your views here.


@api_view(["POST"])
def submit_investor_offer(request):
    if request.method == "POST":
        loan_request = LoanRequest.objects.get(id=request.data['loan_request_id'])
        investor_information = Investor.objects.get(id = request.data['investor_id'])
        investor_balance = investor_information.balance
        if investor_balance < loan_request.loan_amount:
            return Response("There is no sufficient balance ")
        serializer = InvestorOfferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
