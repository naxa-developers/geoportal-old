from rest_framework import serializers

from datasets.models import Apps


class AppsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apps
        exclude = ()