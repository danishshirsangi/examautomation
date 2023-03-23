from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page,name="homepage"),
    #API EndPoint 
    path('demo/<str:usn>/', views.student_fetch,name="fetchdetails"),
]