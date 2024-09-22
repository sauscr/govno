from rest_framework.test import APITestCase
from rest_framework import status

from .models import TableOne, InitialData
from .serializers import TableOneSerializer

from django.urls import reverse

class TableOneAPITest(APITestCase):
    
    def setUp(self):
        '''Подготовка данных перед тестом'''
        self.initial_data = InitialData.objects.create(
            indicator_name='Test Indicator',
            unit='%',
            plan_value=100,
            event_name='Test Event',
            rf_set=100,
            rb_set=50,
            mb_set=30,
            vnb_set=20,
            time_execution_plan=1,
            expected_result='OK',
        )
        
        self.table_one_data = TableOne.objects.create(
            actual_value=90,
            diff_reason='Test Reason',
            init=self.initial_data
        )

    def test_get_table_one(self):
        '''Тест GET запроса для TableOne'''
        url = reverse('indicator_one')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_post_table_one(self):
        '''Тест POST запроса для создания TableOne'''
        url = reverse('indicator_one')
        data = {
            'actual_value': 95,
            'diff_reason': 'Another Test Result',
            'init': self.initial_data.id,
        }
        response = self.client.post(url, data, format='json')
        new_table_one = TableOne.objects.last()
        serializer = TableOneSerializer(new_table_one)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TableOne.objects.count(), 2)
        self.assertEqual(serializer.data['result'], 'Не достигнут')
        expected_deviation = round(
            abs(((self.initial_data.plan_value - new_table_one.actual_value)\
                  / self.initial_data.plan_value) * 100), 2)
        self.assertEqual(
            serializer.data['calculate_relative_deviation'], expected_deviation
        )