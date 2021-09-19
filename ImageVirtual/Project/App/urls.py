from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('upload/', views.upload_img, name='upload'),
    path('home/', views.home, name='home'),
]
