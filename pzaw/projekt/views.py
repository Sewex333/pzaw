from django.http import HttpResponse

def home(request):
    return HttpResponse("Programista lvl 100")
