from django.contrib.gis import admin
from .models import Dataset, Feature, AttributeValue, Attribute


admin.site.register(Dataset, admin.ModelAdmin)
admin.site.register(Feature, admin.GeoModelAdmin)
admin.site.register(Attribute, admin.ModelAdmin)
admin.site.register(AttributeValue, admin.ModelAdmin)