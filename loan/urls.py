from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# URLConf
router = DefaultRouter()
router.register("", views.LoanViewSet)

urlpatterns = [path("accept_offer/", views.accept_offer)]+router.urls
