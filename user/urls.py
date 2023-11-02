from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    #path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>', views.profile_detail, name='profile_detail'),
    path('profile/write', views.profile_write, name='profile_write'),
    path('profile/edit/<int:pk>/', views.profile_edit, name='profile_edit'),
    path('cube_history/', views.cube_history, name = 'cube_history')
]