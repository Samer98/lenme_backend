from rest_framework.routers import DefaultRouter
from .views import BorrowerViewSet

router = DefaultRouter()
router.register("",BorrowerViewSet)

urlpatterns = router.urls
