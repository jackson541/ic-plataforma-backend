from django.urls import path, include
from .views import *

urlpatterns = [
    path('salesman', SalesmanView.as_view()),
    path('client', ClientView.as_view()),
]