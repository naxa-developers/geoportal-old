from django.contrib.auth.models import Group, Permission, User

from rest_framework import serializers

from datasets.models import Department


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = ('id', 'name')


class AddRoleSerializer(serializers.ModelSerializer):
    permissions_list = serializers.ListField(write_only=True)

    class Meta:
        model = Group
        fields = ('name', 'permissions_list')


class AdminSerializer(serializers.ModelSerializer):
    group = serializers.ChoiceField(choices=list(Group.objects.all().values_list('id', flat=True)), write_only=True)

    department = serializers.ChoiceField(choices=list(Department.objects.all().values_list('id', flat=True)),
                                         write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email', 'department', 'group')