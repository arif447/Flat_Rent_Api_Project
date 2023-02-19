from django.urls import path
from flat import views
app_name = 'flat'

urlpatterns = [
    path('addflat/', views.add_flat.as_view(), name='add_flat'),
    path('detailsflat/<id>/', views.update_flat.as_view(), name='details_flat'),
    path('addcategory/', views.add_category.as_view(), name='add_category'),
    path('updatecategory/<id>/', views.update_category.as_view(), name='update_category'),
]