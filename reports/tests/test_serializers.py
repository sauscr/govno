from django.test import TestCase
from ..models import InitialData, TableOne, TableTwo, TableThree
from ..serializers import (
    InitialDataSerializer,
    TableOneSerializer,
    TableTwoSerializer,
    TableThreeSerializer
)


class InitialDataSerializerTest(TestCase):

    def setUp(self):
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
        self.serializer = InitialDataSerializer(instance=self.initial_data)

    def test_contains_expected_fields(self):
        """Проверка наличия всех ожидаемых полей."""
        data = self.serializer.data
        expected_fields = [
            'indicator_name',
            'unit',
            'plan_value',
            'event_name',
            'rf_set',
            'rb_set',
            'mb_set',
            'vnb_set',
            'time_execution_plan',
            'expected_result',
        ]
        self.assertEqual(set(data.keys()), set(expected_fields))

    def test_field_content(self):
        """Проверка содержимого полей."""
        data = self.serializer.data
        self.assertEqual(data['indicator_name'], 'Test Indicator')
        self.assertEqual(data['unit'], '%')
        self.assertEqual(data['plan_value'], 100)
        self.assertEqual(data['event_name'], 'Test Event')
        self.assertEqual(data['rf_set'], 100)
        self.assertEqual(data['rb_set'], 50)
        self.assertEqual(data['mb_set'], 30)
        self.assertEqual(data['vnb_set'], 20)
        self.assertEqual(data['time_execution_plan'], 1)
        self.assertEqual(data['expected_result'], 'OK')


class TableOneSerializerTest(TestCase):

    def setUp(self):
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
        self.serializer = TableOneSerializer(instance=self.table_one)

    def test_contains_expected_fields(self):
        """Проверка наличия всех ожидаемых полей."""
        data = self.serializer.data
        expected_fields = [
            'actual_value',
            'diff_reason',
            'init',
            'result',
            'calculate_relative_deviation',
        ]
        self.assertEqual(set(data.keys()), set(expected_fields))

    def test_field_content(self):
        """Проверка содержимого полей."""
        data = self.serializer.data
        self.assertEqual(data['actual_value'], 90)
        self.assertEqual(data['diff_reason'], 'Test Reason')
        self.assertEqual(data['init'], self.initial_data.id)
        self.assertEqual(data['result'], 'Не достигнут')
        expected_deviation = round(abs(((self.initial_data.plan_value - self.table_one.actual_value) / self.initial_data.plan_value) * 100), 2)
        self.assertEqual(data['calculate_relative_deviation'], expected_deviation)

    def test_serializer_validation(self):
        """Проверка валидации сериализатора при десериализации."""
        data = {
            'actual_value': 95,
            'diff_reason': 'Another Test Result',
            'init': self.initial_data.id,
        }
        serializer = TableOneSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        obj = serializer.save()
        self.assertEqual(obj.actual_value, 95)
        self.assertEqual(obj.diff_reason, 'Another Test Result')
        self.assertEqual(obj.init, self.initial_data)


class TableTwoSerializerTest(TestCase):

    def setUp(self):
        self.initial_data = InitialData.objects.create(
            indicator_name='Test Indicator',
            unit='%',
            plan_value=200,  # Изменил на 200 для суммирования
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
        self.serializer = TableTwoSerializer(instance=self.table_two)

    def test_contains_expected_fields(self):
        """Проверка наличия всех ожидаемых полей."""
        data = self.serializer.data
        expected_fields = [
            'rf_actually',
            'rb_actually',
            'mb_actually',
            'vnb_actually',
            'init',
            'planned_sum',
            'actual_sum',
            # 'calculate_ratio_mastered_to_unmastered',
        ]
        self.assertEqual(set(data.keys()), set(expected_fields))

    def test_field_content(self):
        """Проверка содержимого полей."""
        data = self.serializer.data
        self.assertEqual(data['rf_actually'], 90)
        self.assertEqual(data['rb_actually'], 40)
        self.assertEqual(data['mb_actually'], 20)
        self.assertEqual(data['vnb_actually'], 10)
        self.assertEqual(data['init'], self.initial_data.id)
        self.assertEqual(data['planned_sum'], 200)  # 100 + 50 + 30 + 20
        self.assertEqual(data['actual_sum'], 160)   # 90 + 40 + 20 + 10

    def test_serializer_validation(self):
        """Проверка валидации сериализатора при десериализации."""
        data = {
            'rf_actually': 95,
            'rb_actually': 45,
            'mb_actually': 25,
            'vnb_actually': 15,
            'init': self.initial_data.id,
        }
        serializer = TableTwoSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        obj = serializer.save()
        self.assertEqual(obj.rf_actually, 95)
        self.assertEqual(obj.rb_actually, 45)
        self.assertEqual(obj.mb_actually, 25)
        self.assertEqual(obj.vnb_actually, 15)
        self.assertEqual(obj.init, self.initial_data)


class TableThreeSerializerTest(TestCase):

    def setUp(self):
        self.initial_data = InitialData.objects.create(
            indicator_name='Test Indicator',
            unit='%',
            plan_value=100,
            event_name='Мероприятие «Executor Name»',
            rf_set=100,
            rb_set=50,
            mb_set=30,
            vnb_set=20,
            time_execution_plan=10,
            expected_result='OK',
        )
        self.table_three = TableThree.objects.create(
            time_execution_actually=8,
            actual_result='Good',
            init=self.initial_data
        )
        self.serializer = TableThreeSerializer(instance=self.table_three)

    def test_contains_expected_fields(self):
        """Проверка наличия всех ожидаемых полей."""
        data = self.serializer.data
        expected_fields = [
            'time_execution_actually',
            'actual_result',
            'init',
            'executor',
            'result',
            'percent',
        ]
        self.assertEqual(set(data.keys()), set(expected_fields))

    def test_field_content(self):
        """Проверка содержимого полей."""
        data = self.serializer.data
        self.assertEqual(data['time_execution_actually'], 8)
        self.assertEqual(data['actual_result'], 'Good')
        self.assertEqual(data['init'], self.initial_data.id)
        self.assertEqual(data['executor'], 'Executor Name')
        self.assertEqual(data['result'], 'Достигнут')
        expected_percent = round((8 / 10) * 100, 2)
        self.assertEqual(data['percent'], expected_percent)

    def test_serializer_validation(self):
        """Проверка валидации сериализатора при десериализации."""
        data = {
            'time_execution_actually': 9,
            'actual_result': 'Better',
            'init': self.initial_data.id,
        }
        serializer = TableThreeSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        obj = serializer.save()
        self.assertEqual(obj.time_execution_actually, 9)
        self.assertEqual(obj.actual_result, 'Better')
        self.assertEqual(obj.init, self.initial_data)
