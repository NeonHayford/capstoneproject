from rest_framework import serializers
from .models import *

class categorySerializer(serializers.ModelSerializer):

    class Meta:
        models = category
        fields = '__all__'


class menuserializer(serializers.ModelSerializer):

    class Meta:
        models = menu
        fields = '__all__'

class cartserializer(serializers.ModelSerializer):

    class Meta:
        models = cart
        fields = ('cartid', )
        unique_together = ('user', 'cartid',)


class bookingserializer(serializers.ModelSerializer):

    class Meta:
        models = booking
        fields = '__all__'
        verbose_name = ('Booking')
        verbose_name_plural = ('Bookings')
    pass

class deliveryserializer(serializers.ModelSerializer):
    totalprice = serializers.SerializerMethodField('total_price', read_only=True)

    class Meta:
        models = delivery
        fields = '__all__'
        verbose_name = ('Delivery')

    def total_price(self, obj, args, kwargs):
        return (
            item.price * item.quantity for item in delivery.objects.filter(
            *args, **kwargs
            )
        )


