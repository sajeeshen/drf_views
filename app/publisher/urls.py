from django.urls import path, include
from .views import PublisherViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('publisher', PublisherViewSet)
urlpatterns = [
    path('', include(router.urls)),
]