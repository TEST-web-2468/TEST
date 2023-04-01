from django.urls import path
from django.http import HttpResponse as http
from . import views as v 



urlpatterns = [
    path('test/<str:val>/<str:va>/' , v.test )
]