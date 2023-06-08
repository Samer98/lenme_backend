from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# URLConf
router = DefaultRouter()
router.register("", views.LoanRequestViewSet)

urlpatterns = [path("submitBorrowerRequest/", views.submit_borrower_request)]\
              +router.urls
