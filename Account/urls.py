from django.urls import path, include
from Account import views

app_name = 'Account'

urlpatterns = [
    path('createuser/', views.create_user.as_view(), name='create_user'),
    path('userlist/', views.user_list.as_view(), name='user_list'),
    path('userprofile/', views.user_profile.as_view(), name='user_profile'),
    path('profileupdate/<id>/', views.user_profile_update.as_view(), name='profile_update'),
]
