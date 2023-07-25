from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('admin/', , name=''),
    path('create/category', createcategoryView.as_view(), name='add_category'),
    path('update/<str:pk>/category', updatecategoryView.as_view(), name='update_category'),
    path('delete/<str:pk>/category', deletecategoryView.as_view(), name='delete_category'),

    path('create/menu', createmenuView.as_view(), name='add_menu'),
    path('update/<str:pk>/menu', updatemenuView.as_view(), name='update_menu'),
    path('delete/<str:pk>/menu', deletemenuView.as_view(), name='delete_menu'),

    path('create/cart', createcartView.as_view(), name='add_cart'),
    path('delete/<str:pk>/cart', deletecartView.as_view(), name='delete_cart'),

    path('create/bookings', createbookingView.as_view(), name='add_booking'),
    path('update/<str:pk>/bookings', updatebookingView.as_view(), name='update_booking'),
    path('delete/<str:pk>/bookings', deletebookingView.as_view(), name='delete_booking'),

    path('create/delivery', createdeliveryView.as_view(), name='delivery'),
    path('update/<str:pk>/delivery', updatedeliveryView.as_view(), name='update_delivery'),
    path('api-token-auth/', obtain_auth_token),
]