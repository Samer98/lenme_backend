from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import  LoanRequest
from .serializer import *
from rest_framework.viewsets import ModelViewSet , GenericViewSet
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin, CreateModelMixin, UpdateModelMixin


class LoanRequestViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanSerializers


@api_view(["POST"])
def submit_borrower_request(request):
    if request.method == "POST":
        serializer = LoanSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
