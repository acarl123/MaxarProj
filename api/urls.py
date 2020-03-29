from django.urls import path, include
from rest_framework import routers

from api.viewsets.intersectviewset import InterSectViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(r'intersect/', InterSectViewSet.as_view({'get': 'get', 'post': 'post'}), name="intersect"),
]