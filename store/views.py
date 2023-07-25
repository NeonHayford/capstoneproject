from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import *
from .serializer import *
from rest_framework.decorators import api_view, permission_classes


# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})

# Create your views here.
def index(request):
    return render(request, 'store/index.html')
# Category
class createcategoryView(ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = categorySerializer

class updatecategoryView(UpdateAPIView):
    queryset = category.objects.all()
    serializer_class = categorySerializer

class deletecategoryView(DestroyAPIView):
    queryset = category.objects.all()
    serializer_class = categorySerializer


# Menu
class createmenuView(ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuserializer

class updatemenuView(UpdateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuserializer

class deletemenuView(DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = menuserializer


# Cart
class createcartView(ListCreateAPIView):
    queryset = cart.objects.all()
    serializer_class = cartserializer

class deletecartView(DestroyAPIView):
    queryset = cart.objects.all()
    serializer_class = cartserializer


# Order
class createbookingView(ListCreateAPIView):
    queryset = booking.objects.all()
    serializer_class = bookingserializer

class updatebookingView(UpdateAPIView):
    queryset = booking.objects.all()
    serializer_class = bookingserializer

class deletebookingView(DestroyAPIView):
    queryset = booking.objects.all()
    serializer_class = bookingserializer


# Delivery
class createdeliveryView(ListCreateAPIView):
    queryset = delivery.objects.all()
    serializer_class = deliveryserializer

class updatedeliveryView(UpdateAPIView):
    queryset = delivery.objects.all()
    serializer_class = deliveryserializer


