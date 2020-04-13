from rest_framework import viewsets

from api.permissions import SuperAdminPermission
from api.serializers.DataSetModuleSerializer import AppsSerializer
from datasets.models import Apps


class AppsViewSet(viewsets.ModelViewSet):
    permission_classes = (SuperAdminPermission,)
    serializer_class = AppsSerializer
    queryset = Apps.objects.all()
