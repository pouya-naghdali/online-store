from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.


def http_test(request):
    return render(request,'http-test.html')

def jason_test(request):
    return render(request,'jason-test.html')

def contact(request):
    return render(request,'contact.html')