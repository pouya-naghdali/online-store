from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.


def http_test(request):
    return HttpResponse('http-test page')

def jason_test(request):
    return JsonResponse({
        'name':'sina',
        'color':'black',
        'age':'26',
    })

def contact(request):
    return HttpResponse('contact page of sina \n phone number: 09032535769')