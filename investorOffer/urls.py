from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# URLConf
router = DefaultRouter()
router.register("", views.InvestorOfferViewSet)

urlpatterns = [path("submit_investor_offer/", views.submit_investor_offer)]+router.urls
