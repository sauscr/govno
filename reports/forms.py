# reports/forms.py
from django import forms
from .models import TableOne, TableTwo, TableThree, InitialData



class CleanMixin:
    '''
    Метод для проверки обязательных полей и значений.
    '''
    required_fields = []

    def clean(self):
        cleaned_data = super().clean()

        for field in self.required_fields:
            if cleaned_data.get(field) is None:
                raise forms.ValidationError(
                    f'Значение {field} не может быть отрицательным.')
            if cleaned_data.get(field) < 0:
                raise forms.ValidationError(
                    f'Поле {field} должно быть заполнено.')
        
        return cleaned_data

class InitialDataForm(CleanMixin, forms.Form):
    '''
    Форма для заполнения инициализируемых данных.
    '''
    required_fields = ['plan_value', 'rf_set', 'mb_set',
                       'vnb_set', 'time_execution_plan',]

    class Meta:
        model = InitialData
        fields = ['indicator_name', 'unit', 'event_name',
                  'plan_value','rf_set', 'mb_set', 'vnb_set',
                  'time_execution_plan', 'expected_result']


class TableOneForm(CleanMixin, forms.ModelForm):
    '''
    Форма для модели первой таблицы.
    '''
    required_fields = ['actual_value', ]

    class Meta:
        model = TableOne
        fields = ['actual_value', 'diff_reason',]
    

class TableTwoForm(CleanMixin, forms.ModelForm):
    '''
    Форма для модели второй таблицы.
    '''
    required_fields = ['rf_actually', 'mb_actually', 'vnb_actually',]
    
    class Meta:
        model = TableTwo
        fields = ['rf_actually', 'mb_actually', 'vnb_actually',]


class TableThreeForm(CleanMixin, forms.ModelForm):
    '''
    Форма для модели третьей таблицы.
    '''
    required_fields = ['time_execution_actually',]
    
    class Meta:
        model = TableThree
        fields = ['time_execution_actually', 'actual_result',]

