import re
from django.db.models import F, ExpressionWrapper, FloatField, CharField

def calculate_relative_deviation(plan_value, actual_value):
    '''
    Вычисляет относительную дивергенцию между двумя значениями.
    '''
    return ExpressionWrapper(
        (F(plan_value) - F(actual_value)) / F(plan_value) * 100,
        output_field=FloatField()
    )
        
def calculate_ratio_mastered_to_unmastered(value1, value2):
    '''
    Вычисляет % выполнения.
    '''
    if value1 is not None and value1 != 0:
        return round((value1 / value2) * 100, 2)
    return None


def result(plan_value, actual_value):
    '''
    Методы, связанные с определением результатов.
    '''
    if plan_value > actual_value:
        return 'Не достигнут', CharField()
    else:
        return 'Достигнут', CharField()
        

def extract_text(text):
    '''
    Поиска текста между двойными кавычками в строке.
    '''
    pattern = r'«(.*?)»'
    much = re.search(pattern, text)
    if much:
        return much.group(1)
    return None
