import requests
from django.http import JsonResponse

def call_fastapi(request):
    response = requests.get("http://localhost:8000/api")
    return JsonResponse(response.json())
