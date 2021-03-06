from django.urls import path, include
from .views import homeView, sign_in, logout, sign_up, upload_bot, bot_details, bot_page, profile

urlpatterns = [
    path('', homeView, name="home"),
    path('sign_in/', sign_in, name="sign_in"),
    path('logout/', logout, name="logout"),
    path('sign_up/', sign_up, name="sign_up"),
    path('upload/', upload_bot, name="upload"),
    path('bot/<int:pk>/', bot_details, name="bot_details"),
    path('bots/', bot_page, name="bots"),
    path('bots/profile', profile, name="profile_page" )
]



