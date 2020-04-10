import ast

from django.contrib.auth.models import Group, Permission
from django.db import transaction

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.permissions import SuperAdminPermission
from api.serializers.UserModuleSerializer import AddRoleSerializer, PermissionSerializer


class RoleListView(APIView):
    permission_classes = (SuperAdminPermission,)

    def get(self, *args, **kwargs):
        groups = Group.objects.all()
        all_permissions = Permission.objects.all().values('id', 'name')
        role_list = []
        for group in groups:
            role_list.append({'id': group.id, 'name': group.name,
                              'permissions': PermissionSerializer(group.permissions.all(), many=True).data})

        return Response(status=status.HTTP_200_OK, data={'role_list': role_list,
                                                         'all_permissions': all_permissions})


class AddRoleView(viewsets.ModelViewSet):
    permission_classes = (SuperAdminPermission,)
    serializer_class = AddRoleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        permissions_list = request.data.get('permissions_list')
        perm_list = ast.literal_eval(permissions_list)
        with transaction.atomic():
            try:
                group = Group.objects.create(name=request.data.get('name'))
                for permission in perm_list:
                    group.permissions.add(int(permission))
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'detail': str(e)})
        return Response(status=status.HTTP_201_CREATED, data={'detail': 'Successfully created Role with permissions'})

