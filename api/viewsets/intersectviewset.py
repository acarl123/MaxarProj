from rest_framework import views, viewsets
from rest_framework.response import Response

from django.http import HttpResponse
from shapely.geometry import Polygon

import geojson


class InterSectViewSet(viewsets.GenericViewSet):
    """
    Simple viewset to return a boolean if 2 geoJSON points intersect
    """
    def post(self, request):
        data = geojson.loads(request.body)
        polygons = []
        for polygon in data.get('features'):
            coords = polygon.get('geometry').get('coordinates')[0]
            polygons.append(Polygon(coords))
        
        if len(polygons) != 2: 
            return HttpResponse(400)

        return Response({'intersect': polygons[0].intersects(polygons[1])})

    def get(self, request):
        return HttpResponse(200)