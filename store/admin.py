from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(category)
admin.site.register(menu)
admin.site.register(cart)
admin.site.register(booking)
admin.site.register(delivery)