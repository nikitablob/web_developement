from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("hELLO WORLD!")

def index(request):
    my_dict = {'insert_me': "i am coming from first_app/help.html"}
    return render(request, "first_app/help.html", context=my_dict)
