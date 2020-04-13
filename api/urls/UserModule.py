from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from api.viewsets.UserModuleViewset import RoleListView, AddRoleView, AddAdminView


user_module_urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('role-list/', RoleListView.as_view(), name='role_list'),
    path('add-role/', AddRoleView.as_view({'post': 'create'}), name='add_role'),
    path('add-admin/', AddAdminView.as_view({'post': 'create'}), name='add_admin'),

]