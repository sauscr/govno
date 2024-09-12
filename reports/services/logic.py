

class CalculationServices:
    
    @staticmethod
    def calculate_relative_diviation(plan_value, actual_value):
        if plan_value != 0:
            return round(abs(((actual_value - plan_value) / plan_value) * 100), 2)
        return None
    
    @staticmethod
    def result(plan_value, actual_value):
        if plan_value > actual_value:
            return 'Не достигнут'
        else:
            return 'Достигнут'