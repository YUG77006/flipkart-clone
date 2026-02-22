from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mobiles/', views.mobiles, name='mobiles'),
    path('fashion/', views.fashion, name='fashion'),
]