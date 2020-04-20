from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status


class BaseUserModuleCaseMixin(APITestCase):

    def setUp(self):
        user = User.objects.create(username="test_user")
        user.set_password('test_pw')
        user.is_superuser = True
        user.save()
        self.data = {'username': 'test_user',
                     'password': 'test_pw'
                     }
        self.token_url = reverse('api:token_obtain_pair')

        self.response = self.client.post(self.token_url, self.data, format='json')
        self.api_authentication()

    def api_authentication(self):

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.response.data['access'])


class AddRoleViewTestCase(BaseUserModuleCaseMixin):

    def test_add_role_response(self):
        """
            Test to verify if the response is correct.
        """
        self.add_role_url = reverse('api:add_role')
        self.response = self.client.get(self.add_role_url)
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, self.response.status_code)
