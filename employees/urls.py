from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('<int:pk>/',views.employee_details,name='employee_details'),
]