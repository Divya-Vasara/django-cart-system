from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CartViewSet

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('api/', include(router.urls)),
]