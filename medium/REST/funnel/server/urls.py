from django.conf.urls import url
from rest_framework import routers
from funnel.server.views import ServerViewSet

router = routers.DefaultRouter()
router.register(r'server', ServerViewSet)

urlpatterns = router.urls
