from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('addcart/', views.add_cart.as_view(), name='add_cart'),
    path('updatecart/<id>/', views.update_cart.as_view(), name='update_cart'),
    path('order/', views.make_order.as_view(), name='make_order'),
    path('updateorder/<id>/', views.update_order.as_view(), name='update_order'),
]
