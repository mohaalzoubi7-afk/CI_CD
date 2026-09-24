from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Hello from the CI/CD demo!",
        "status": "running",
    })
