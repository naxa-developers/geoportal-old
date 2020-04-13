import os, argparse, sys

from django.contrib.gis.geos import GEOSGeometry
from osgeo import ogr, osr

from django.core.management.base import BaseCommand

from datasets.models import Dataset, Feature, Attribute
from datasets.utils import wrap_geos_geometry, calc_geometry_field, get_ogr_feature_attribute


class Command(BaseCommand):
    help = 'upload shape file or tiff file.'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        dir_name = sys.argv[3]
        shapefile_name = 'hydro ln'

        # datasource = ogr.Open(os.path.join(dir_name, shapefile_name))
        datasource = ogr.Open(dir_name)

        layer = datasource.GetLayer(0)

        # creating Dataset object

        src_spatial_ref = layer.GetSpatialRef()
        geom_type = layer.GetLayerDefn().GetGeomType()
        geom_name = ogr.GeometryTypeToName(geom_type)
        shapefile = Dataset(name=shapefile_name, srs_wkt=src_spatial_ref.ExportToWkt(), geom_type=geom_name)
        shapefile.save()

        # creating Attribute objects

        attributes = []
        layer_def = layer.GetLayerDefn()
        for i in range(layer_def.GetFieldCount()):
            field_def = layer_def.GetFieldDefn(i)
            attr = Attribute(dataset=shapefile,
                             name=field_def.GetName(),
                             type=field_def.GetType(),
                             width=field_def.GetWidth(),
                             precision=field_def.GetPrecision())
            attributes.append(attr)
        Attribute.objects.bulk_create(attributes)

        # creating Feature objects

        dst_spatial_ref = osr.SpatialReference()
        dst_spatial_ref.ImportFromEPSG(4326)
        coord_transform = osr.CoordinateTransformation(
            src_spatial_ref,
            dst_spatial_ref)
        feature_objs = []

        for i in range(layer.GetFeatureCount()):
            src_feature = layer.GetFeature(i)
            src_geometry = src_feature.GetGeometryRef()
            src_geometry.Transform(coord_transform)
            geometry = GEOSGeometry(src_geometry.ExportToWkt())
            geometry = wrap_geos_geometry(geometry)
            geom_field = calc_geometry_field(geom_name)
            fields = {}
            fields['dataset'] = shapefile
            fields[geom_field] = geometry

            attribute_dict = dict()
            for attr in attributes:

                success, result = get_ogr_feature_attribute(
                    attr, src_feature)
                if not success:
                    # os.remove(fname)
                    # shutil.rmtree(dir_name)
                    shapefile.delete()
                    return result
                attribute_dict.update({attr.name: result})

            fields['attribute_values'] = attribute_dict
            feature = Feature(**fields)
            feature_objs.append(feature)

        Feature.objects.bulk_create(feature_objs)

        self.stdout.write('Successfully loaded datasets.')
