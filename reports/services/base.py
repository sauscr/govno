class JoinServices:
    '''
    Сервис для join запросов в БД.
    '''

    def __init__(self, model_a, model_b, fields):
        self.model_a = model_a
        self.model_b = model_b
        self.fields = fields

    def get_joined_data(self):
        return self.model_a.objects.\
            select_related(self.model_b).values(*self.fields)