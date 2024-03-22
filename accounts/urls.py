from django.urls import path
from . import views

urlpatterns = [
    path('signupaccount', views.signupaccount, name='vspAccountSignup'),
    path('logout', views.logoutaccount, name='vspAccountLogout'),
    path('login/', views.loginaccount, name='vspAccountLogin'),
]
