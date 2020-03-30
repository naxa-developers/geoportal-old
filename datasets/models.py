from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager


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
    objects = GeoManager()

    def __str__(self):
        return str(self.id)


class AttributeValue(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name="attr_values")
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name="attr_values")
    value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.value