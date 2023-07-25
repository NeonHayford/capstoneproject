from django.shortcuts import render
from .models import menu

def bookingView(request):
    class Meta:
        models = menu
        fields ='__all__'