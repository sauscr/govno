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