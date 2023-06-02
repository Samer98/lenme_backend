from django.shortcuts import render
from .serializers import BorrowerSerializers
from .models import Borrower
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class BorrowerViewSet(ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializers
