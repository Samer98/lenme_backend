from django.shortcuts import render
from rest_framework.viewsets import  ModelViewSet , GenericViewSet
from .serializer import *
from .models import Installment

# Create your views here.
class InstallmentsViewSet(ModelViewSet):
    queryset =  Installment.objects.all()
    serializer_class = InstallmentSerializer
