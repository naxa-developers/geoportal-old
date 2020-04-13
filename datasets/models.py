from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from django.contrib.postgres.fields import JSONField


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Dataset(models.Model):
    name = models.CharField(max_length=255)
    srs_wkt = models.CharField(max_length=255)
    geom_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name="attributes")
    name = models.CharField(max_length=255)
    type = models.IntegerField()
    width = models.IntegerField()
    precision = models.IntegerField()

    def __str__(self):
        return self.name


class Feature(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name="features")
    raster = models.RasterField(null=True, blank=True)
    geom_point = models.PointField(srid=4326, blank=True, null=True)
    geom_multipoint = models.MultiPointField(srid=4326, blank=True, null=True)
    geom_multilinestring = models.MultiLineStringField(srid=4326, blank=True, null=True)
    geom_multipolygon = models.MultiPolygonField(srid=4326, blank=True, null=True)
    geom_geometrycollection = models.GeometryCollectionField(srid=4326, blank=True, null=True)
    attribute_values = JSONField(default=dict)
    objects = GeoManager()

    def __str__(self):
        return str(self.id)


class Apps(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    photo = models.ImageField(upload_to="apps/", null=True, blank=True)

    def __str__(self):
        return self.title