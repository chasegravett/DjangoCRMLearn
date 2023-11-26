from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('users/', views.show_users, name='users'),
    path('users_sorted_first_name/', views.show_users_sorted_firstname, name='users_sorted_first_name'),
    path('users_sorted_last_name/', views.show_users_sorted_lastname, name='users_sorted_last_name'),
    path('users_sorted_creation/', views.show_users_sorted_creation, name='users_sorted_creation'),
    path('users_sorted_street/', views.show_users_sorted_street, name='users_sorted_street'),
    path('users_sorted_state/', views.show_users_sorted_state, name='users_sorted_state'),
    path('users_sorted_email/', views.show_users_sorted_email, name='users_sorted_email'),
    path('users_sorted_phone/', views.show_users_sorted_phone, name='users_sorted_phone'),
]