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

        return Response({'intersect': polygons[0].intersects(polygons[1])})
    
    def validate_geojson(self, request):
        data = geojson.loads(request.body)
        try:
            featureCollection = geojson.FeatureCollection(data)
            featureCollection.is_valid
            if not len(featureCollection['features']) == 2:
                return Response({'error': 'Incorrect number of polygons'})
        except AttributeError:
            return Response({'error': 'Invalid geoJSON'})
        return Response({})

    def get(self, request):
        return HttpResponse(200)