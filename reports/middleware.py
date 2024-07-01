from django.apps import apps
from django.conf import settings

class LoadDataMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.models_to_load = getattr(settings, 'MODEL_NAMES', [])

    def __call__(self, request):
        for model_name in self.models_to_load:
            model = apps.get_model('reports', model_name)
            setattr(request, model_name.lower() + 's', model.objects.all())
        response = self.get_response(request)
        return response
# Middleware - это класс, который может быть добавлен в Django-приложение, чтобы выполнять определенные действия при обработке каждого запроса.
# В данном случае, LoadDataMiddleware выполняет следующие действия:

# 1. Во время инициализации, LoadDataMiddleware получает список моделей, которые нужно загрузить из настроек приложения.
# 2. При каждом запросе, LoadDataMiddleware получает все объекты для каждой модели и добавляет их в контекст запроса.
# 3. Затем LoadDataMiddleware передает запрос в следующий обработчик.

# Комментарии:
# - __init__ - инициализация Middleware. Здесь мы получаем функцию next_middleware из аргументов и список моделей, которые нужно загрузить.
# - __call__ - метод, который выполняет все действия Middleware.
# - apps.get_model используется для получения модели по имени и приложению.
# - setattr используется для добавления атрибута объекта, в данном случае, добавления списка объектов модели в контекст запроса.
