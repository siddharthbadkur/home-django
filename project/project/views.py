from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>welcome to home page</h1>')
