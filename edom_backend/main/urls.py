from rest_framework import routers

from main.views import DeveloperViewSet

router = routers.DefaultRouter()
router.register(r"developers", DeveloperViewSet)
