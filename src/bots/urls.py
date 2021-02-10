from django.urls import path, include
from .views import homeView, sign_in, logout, sign_up

urlpatterns = [
    path('', homeView, name="home"),
    path('sign_in/', sign_in, name="sign_in"),
    path('logout/', logout, name="logout"),
    path('sign_up/', sign_up, name="sign_up")
]



