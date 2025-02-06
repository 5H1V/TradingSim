from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, index.")

def login(request):
    return HttpResponse("Hello, login.")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
