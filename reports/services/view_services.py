def get_values(data_list, fields):
    '''
    Возвращает данные из модели в виде списка словарей
    '''
    return [
        {field: getattr(item, field) for field in fields}
        for item in data_list
    ]


def get_all_objects(model):
    return model.objects.all()