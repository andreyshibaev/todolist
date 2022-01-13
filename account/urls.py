from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register_account, name='signupuser'),
    path('login/', views.login_account, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
]