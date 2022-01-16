from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello world")

def help(request):
    my_dict = {"help_insert": "HELP PAGE"}
    return render(request, "sec_app/help.html", context=my_dict)


