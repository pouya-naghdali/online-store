from django.urls import path
from website_app.views import http_test,jason_test,contact

urlpatterns = [
    path('http-test',http_test),
    path('jason-test',jason_test),
    path('contact',contact)
]