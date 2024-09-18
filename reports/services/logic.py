import re

def calculate_relative_diviation(value1, value2):
    '''
    Вычисление относительной дивергенции между двумя значениями.
    '''
    if value1 is not None and value1 != 0:
        return round(abs(((value1 - value2) / value1) * 100), 2)
    return None
        
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
        return 'Не достигнут'
    else:
        return 'Достигнут'
        

def extract_text(text):
    '''
    Поиска текста между двойными кавычками в строке.
    '''
    pattern = r'«(.*?)»'
    much = re.search(pattern, text)
    if much:
        return much.group(1)
    return None
