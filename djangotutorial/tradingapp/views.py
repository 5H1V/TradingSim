from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, you are at the homepage.")

def login(request):
    return HttpResponse("Hello, you are at the login page.")
