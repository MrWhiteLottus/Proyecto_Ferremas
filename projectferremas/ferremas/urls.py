from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductosViewSet, productos_page

router = DefaultRouter()
router.register(r'ferremas', ProductosViewSet)

urlpatterns = [
    path('ferremas/', productos_page, name='productos-page'),
    path('', include(router.urls)),

]