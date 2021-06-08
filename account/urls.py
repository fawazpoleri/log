from django.urls import path
from . import views

urlpatterns = [
    path('login_view/', views.login_view,name="login"),  
      
    path('staffhome/', views.staffhome,name="staffhome"),    
    path('studenthome/', views.studenthome,name="studenthome"),    
      
]