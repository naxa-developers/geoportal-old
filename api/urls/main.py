from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from api.views import HelloView
from api.urls.UserModule import user_module_urlpatterns

app_name = 'api'

urlpatterns = [
    path('test-api/', HelloView.as_view(), name="test")

]

urlpatterns += user_module_urlpatterns
