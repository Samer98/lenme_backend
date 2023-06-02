from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin , UpdateModelMixin
from .models import Investor
from .serializers import InvestorSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet


# Create your views here.

class InvestorViewSet(ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
