import ast

from django.contrib.auth.models import Group, Permission

from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = ('id', 'name')


class AddRoleSerializer(serializers.ModelSerializer):
    permissions_list = serializers.ListField(write_only=True)

    class Meta:
        model = Group
        fields = ('name', 'permissions_list')