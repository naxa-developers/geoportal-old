from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from datasets.models import Dataset, Attribute
import tempfile, os, shutil, zipfile
from osgeo import ogr, osr
from datasets.utils import calc_geometry_field, unwrap_geos_geometry, set_ogr_feature_attribute
from django.http import FileResponse


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Successfully implemented JWT '}
        return Response(content)


def export(request, id):
    shapefile = Dataset.objects.get(id=id)
    dst_dir = tempfile.mkdtemp()

    dst_file = str(os.path.join(dst_dir, shapefile.name))

    dst_spatial_ref = osr.SpatialReference()
    dst_spatial_ref.ImportFromWkt(shapefile.srs_wkt)
    driver = ogr.GetDriverByName("ESRI Shapefile")
    datasource = driver.CreateDataSource(dst_file + '.shp')
    layer = datasource.CreateLayer(shapefile.name,
                                   dst_spatial_ref)

    for attr in shapefile.attributes.all():
        field = ogr.FieldDefn(attr.name, attr.type)
        field.SetWidth(attr.width)
        field.SetPrecision(attr.precision)
        layer.CreateField(field)

    src_spatial_ref = osr.SpatialReference()
    src_spatial_ref.ImportFromEPSG(4326)
    coord_transform = osr.CoordinateTransformation(
        src_spatial_ref, dst_spatial_ref)
    geom_field = calc_geometry_field(shapefile.geom_type)

    for feature in shapefile.features.all():
        geometry = getattr(feature, geom_field)
        geometry = unwrap_geos_geometry(geometry)

        dst_geometry = ogr.CreateGeometryFromWkt(geometry.wkt)
        dst_geometry.Transform(coord_transform)
        dst_feature = ogr.Feature(layer.GetLayerDefn())
        dst_feature.SetGeometry(dst_geometry)
        dst_feature = ogr.Feature(layer.GetLayerDefn())
        dst_feature.SetGeometry(dst_geometry)

        for attr, val in feature.attribute_values.items():
            attr_obj = Attribute.objects.filter(name=attr, dataset=shapefile)[0]
            set_ogr_feature_attribute(
                attr_obj,
                val,
                dst_feature)
        layer.CreateFeature(dst_feature)
        dst_feature.Destroy()

    datasource.Destroy()  # Close the file, write everything to disk.

    temp = tempfile.TemporaryFile()
    zip = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)

    shapefileName = os.path.splitext(shapefile.name)[0]

    for fName in os.listdir(dst_dir):
        zip.write(os.path.join(dst_dir, fName), fName)

    zip.close()

    shutil.rmtree(dst_dir)

    temp.flush()
    temp.seek(0)

    response = FileResponse(temp)
    response['Content-type'] = "application/zip"
    response['Content-Disposition'] = "attachment; filename=" + shapefileName + ".zip"
    return response