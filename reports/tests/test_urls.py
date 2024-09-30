from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from ..views import InitialDataView, TableOneAPIView, TableTwoAPIView, TableThreeAPIView

class UrlsTestCase(TestCase):

    def test_initial_data_url_resolves(self):
        """Проверка, что URL для InitialDataView правильно разрешается."""
        url = reverse('data_view')  # Получаем URL по имени
        self.assertEqual(resolve(url).func.view_class, InitialDataView)  # Проверка соответствия вью

    def test_table_one_url_resolves(self):
        """Проверка, что URL для TableOneAPIView правильно разрешается."""
        url = reverse('indicator_one')
        self.assertEqual(resolve(url).func.view_class, TableOneAPIView)

    def test_table_two_url_resolves(self):
        """Проверка, что URL для TableTwoAPIView правильно разрешается."""
        url = reverse('indicator_two')
        self.assertEqual(resolve(url).func.view_class, TableTwoAPIView)

    def test_table_three_url_resolves(self):
        """Проверка, что URL для TableThreeAPIView правильно разрешается."""
        url = reverse('indicator_three')
        self.assertEqual(resolve(url).func.view_class, TableThreeAPIView)

    def test_initial_data_url_status_code(self):
        """Проверка, что URL InitialDataView возвращает правильный статус-код."""
        response = self.client.get(reverse('data_view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Ожидаем 200 OK

    def test_table_one_url_status_code(self):
        """Проверка, что URL TableOneAPIView возвращает правильный статус-код."""
        response = self.client.get(reverse('indicator_one'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_table_two_url_status_code(self):
        """Проверка, что URL TableTwoAPIView возвращает правильный статус-код."""
        response = self.client.get(reverse('indicator_two'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_table_three_url_status_code(self):
        """Проверка, что URL TableThreeAPIView возвращает правильный статус-код."""
        response = self.client.get(reverse('indicator_three'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
