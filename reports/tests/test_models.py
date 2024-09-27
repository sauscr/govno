from django.test import TestCase
from ..models import InitialData, TableOne, TableTwo, TableThree


class InitialDataModelTest(TestCase):

    def setUp(self):
        '''Создаем объект InitialData для использования в тестах.'''
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

    def test_initial_data_creation(self):
        '''Проверка успешного создания объекта InitialData.'''
        self.assertEqual(self.initial_data.indicator_name, 'Test Indicator')
        self.assertEqual(self.initial_data.unit, '%')
        self.assertEqual(self.initial_data.plan_value, 100)


class TableOneModelTest(TestCase):

    def setUp(self):
        '''Создаем объект InitialData и TableOne для использования в тестах.'''
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
        self.table_one = TableOne.objects.create(
            actual_value=90,
            diff_reason='Test Reason',
            init=self.initial_data
        )

    def test_table_one_creation(self):
        '''Проверка успешного создания объекта TableOne.'''
        self.assertEqual(self.table_one.actual_value, 90)
        self.assertEqual(self.table_one.diff_reason, 'Test Reason')
        self.assertEqual(self.table_one.init, self.initial_data)


class TableTwoModelTest(TestCase):

    def setUp(self):
        '''Создаем объект InitialData и TableTwo для использования в тестах.'''
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
        self.table_two = TableTwo.objects.create(
            rf_actually=90,
            rb_actually=40,
            mb_actually=20,
            vnb_actually=10,
            init=self.initial_data
        )

    def test_table_two_creation(self):
        '''Проверка успешного создания объекта TableTwo.'''
        self.assertEqual(self.table_two.rf_actually, 90)
        self.assertEqual(self.table_two.rb_actually, 40)
        self.assertEqual(self.table_two.init, self.initial_data)


class TableThreeModelTest(TestCase):

    def setUp(self):
        '''Создаем объект InitialData и TableThree для использования в тестах.'''
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
        self.table_three = TableThree.objects.create(
            time_execution_actually=8,
            actual_result='Good',
            init=self.initial_data
        )

    def test_table_three_creation(self):
        '''Проверка успешного создания объекта TableThree.'''
        self.assertEqual(self.table_three.time_execution_actually, 8)
        self.assertEqual(self.table_three.actual_result, 'Good')
        self.assertEqual(self.table_three.init, self.initial_data)