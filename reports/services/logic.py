
class Math:       
    '''
    Методы, связанные с математическими вычислениями.
    '''

    @staticmethod
    def calculate_relative_diviation(value1, value2):
        '''
        Вычисление относительной дивергенции между двумя значениями.
        '''
        if value1 is not None and value1 != 0:
            return round(abs(((value1 - value2) / value1) * 100), 2)
        return None
        
    @staticmethod
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

    @staticmethod
    def result(plan_value, actual_value):
        if plan_value > actual_value:
            return 'Не достигнут'
        else:
            return 'Достигнут'
        


class UtilityService:
    '''
    Вспомогательные методы.
    '''

    @staticmethod
    def calculate_sums(*args):
        return sum(args)
    