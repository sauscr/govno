# reports/forms.py
from django import forms
from .models import TableOne, TableTwo



class CleanMixin:
    '''g
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


class TableOneForm(CleanMixin, forms.ModelForm):
    '''
    Класс формы для модели первой таблицы.
    '''
    required_fields = ['plan_value', 'actual_value']

    class Meta:
        model = TableOne
        fields = ['name', 'plan_value', 'actual_value', 'diff_reason',]
    

class TableTwoForm(CleanMixin, forms.ModelForm):
    '''
    Класс формы для модели второй таблицы.
    '''
    required_fields = ['rf_set', 'mb_set', 'vnb_set',
                       'rf_actually', 'mb_actually', 'vnb_actually',]
    
    class Meta:
        model = TableTwo
        fields = ['name', 'rf_set', 'mb_set', 'vnb_set',
                  'rf_actually', 'mb_actually', 'vnb_actually',]