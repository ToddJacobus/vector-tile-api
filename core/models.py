from django.contrib.gis.db import models

class Point(models.Model):
    """A simple point model"""
    color = models.CharField(max_length=50)
    geom = models.PointField(srid=4326)

class Line(models.Model):
    """A simple line field"""
    color = models.CharField(max_length=50)
    geom = models.LineStringField(srid=4326)

class Polygon(models.Model):
    """A simple polygon field"""
    color = models.CharField(max_length=50)
    geom = models.PolygonField(srid=4326)
