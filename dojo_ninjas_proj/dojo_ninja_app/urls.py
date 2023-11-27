from django.urls import path
from . import views
urlpatterns = [
    path('', views.method1),
    path('adddojo', views.method2),
    path('addninja', views.method3),
    
]
