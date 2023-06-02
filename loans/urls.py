from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# URLConf
router = DefaultRouter()
router.register("",views.LoanViewSet)

urlpatterns = [path("submitBorrowerRequest/", views.submit_borrower_request),
               path("submitInvestorRequest/<id>",views.submit_investor_request)]\
              +router.urls
