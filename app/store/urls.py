from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import path, include
app_name = 'store'
router = DefaultRouter()
router.register('store', BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]