# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('create_company/', views.create_company, name='create_company'),
    path('my_progect/', views.my_progect, name='my_progect'),
    path('create_affiliater/', views.create_affiliater, name='create_affiliater'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('create_services/', views.create_services, name='create_services'),
    path('services_list', views.services_list, name='services_list')
    path('del_services', views.del_services, name='')
]