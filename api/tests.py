from django.test import TestCase
import json

# Create your tests here.


class IntersectTest(TestCase):
    def setUp(self):
        self.intersectingJsonPolygons = {
            "type": "FeatureCollection",
            "features": [
                {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -105.11392593383789,
                        39.93053755341913
                        ],
                        [
                        -105.12199401855467,
                        39.908287806179985
                        ],
                        [
                        -105.08508682250977,
                        39.90512749255248
                        ],
                        [
                        -105.09641647338867,
                        39.92593021117534
                        ],
                        [
                        -105.11392593383789,
                        39.93053755341913
                        ]
                    ]
                    ]
                }
                },
                {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -105.09899139404297,
                        39.93277529347977
                        ],
                        [
                        -105.10139465332031,
                        39.916319613808135
                        ],
                        [
                        -105.07238388061523,
                        39.91724123641016
                        ],
                        [
                        -105.09899139404297,
                        39.93277529347977
                        ]
                    ]
                    ]
                }
                }
            ]
            }
        
        self.nonIntersectingJsonPolygons = {
            "type": "FeatureCollection",
            "features": [
                {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -105.09899139404297,
                        39.93277529347977
                        ],
                        [
                        -105.10139465332031,
                        39.916319613808135
                        ],
                        [
                        -105.07238388061523,
                        39.91724123641016
                        ],
                        [
                        -105.09899139404297,
                        39.93277529347977
                        ]
                    ]
                    ]
                }
                },
                {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -105.0907516479492,
                        39.898806427947754
                        ],
                        [
                        -105.0761604309082,
                        39.88616254942062
                        ],
                        [
                        -105.06637573242188,
                        39.90078182327698
                        ],
                        [
                        -105.0907516479492,
                        39.898806427947754
                        ]
                    ]
                    ]
                }
                }
            ]
            }

    def test_shouldReturnTrueWhenIntersectingGeoJSON(self):
        response = self.client.post('/api/intersect/', self.intersectingJsonPolygons, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'true')
    
    def test_shouldReturnFalseWhenNonIntersectingGeoJSON(self):
        response = self.client.post('/api/intersect/', self.nonIntersectingJsonPolygons, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'false')