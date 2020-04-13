from rest_framework import routers

from django.urls import path, include

from api.viewsets.DataSetModuleViewset import AppsViewSet

router = routers.DefaultRouter()
router.register(r'apps', AppsViewSet)

dataset_module_urlpatterns = [
    path('', include(router.urls)),

]