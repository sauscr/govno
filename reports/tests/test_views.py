from rest_framework.test import APITestCase
from rest_framework import status

from ..models import InitialData, TableOne, TableTwo, TableThree
from ..serializers import TableOneSerializer, TableTwoSerializer, TableThreeSerializer

from django.urls import reverse

class TableOneAPITest(APITestCase):
    '''
    Тест для вью TableOne
    '''
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


class TableTwoAPITest(APITestCase):

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

        self.table_two_data = TableTwo.objects.create(
            rf_actually=90,
            rb_actually=40,
            mb_actually=20,
            vnb_actually=10,
            init=self.initial_data
        )

    def test_get_table_two(self):
        '''Тест GET запроса для TableTwo'''
        url = reverse('indicator_two')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_table_two(self):
        '''Тест POST запроса для создания TableTwo'''
        url = reverse('indicator_two')
        data = {
            'rf_actually': 95,
            'rb_actually': 45,
            'mb_actually': 25,
            'vnb_actually': 15,
            'init': self.initial_data.id,
        }
        response = self.client.post(url, data, format='json')
        new_table_two = TableTwo.objects.last()
        serializer = TableTwoSerializer(new_table_two)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TableTwo.objects.count(), 2)
        self.assertEqual(serializer.data['planned_sum'], 200)
        # expected_ratio = round((new_table_two.actual_sum / 200) * 100, 2)
        # self.assertEqual(serializer.data['calculate_ratio_mastered_to_unmastered'], expected_ratio)


class TableThreeAPITest(APITestCase):
    '''
    Тест для вью TableOne
    '''
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
            time_execution_plan=10,
            expected_result='OK',
        )

        self.table_three_data = TableThree.objects.create(
            time_execution_actually=8,
            actual_result='Good',
            init=self.initial_data
        )

    def test_get_table_three(self):
        '''Тест GET запроса для TableThree'''
        url = reverse('indicator_three')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_table_three(self):
        '''Тест POST запроса для создания TableThree'''
        url = reverse('indicator_three')
        data = {
            'time_execution_actually': 9,
            'actual_result': 'Better',
            'init': self.initial_data.id,
        }
        response = self.client.post(url, data, format='json')
        new_table_three = TableThree.objects.last()
        serializer = TableThreeSerializer(new_table_three)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TableThree.objects.count(), 2)
        self.assertEqual(serializer.data['result'], 'Достигнут')
        expected_percent = round((new_table_three.time_execution_actually / self.initial_data.time_execution_plan) * 100, 2)
        self.assertEqual(serializer.data['percent'], expected_percent)