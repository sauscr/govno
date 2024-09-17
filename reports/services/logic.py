# убрать лишние классы (оставить просто функции)
class Math:       
    '''
    Методы, связанные с математическими вычислениями.
    '''


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



class ResultService:
    '''
    Методы, связанные с определением результатов.
    '''

    def result(plan_value, actual_value):
        if plan_value > actual_value:
            return 'Не достигнут'
        else:
            return 'Достигнут'
        

