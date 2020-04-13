from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from api.views import HelloView, export
from api.urls.UserModule import user_module_urlpatterns
from api.urls.DatasetModule import dataset_module_urlpatterns

app_name = 'api'

urlpatterns = [
    path('test-api/', HelloView.as_view(), name="test"),
    path('export/<int:id>/', export, name="export")

]

urlpatterns += user_module_urlpatterns
urlpatterns += dataset_module_urlpatterns

