from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, VideoViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'video', VideoViewSet)


urlpatterns = [
 path('', include(router.urls))
]