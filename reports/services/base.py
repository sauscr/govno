from ..models import InitialData


class DataServis:

    @staticmethod
    def get_filtered_data(*fields):
        '''
        Возвращает только указанные поля из модели InitialData.
        '''
        return InitialData.objects.filter(*fields)