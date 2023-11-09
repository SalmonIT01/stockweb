from django.urls import path
from app_home.views import *

urlpatterns = [
<<<<<<< Updated upstream
    path('',views.index,name="index"),
    path('home',views.home,name='home')
    
    
=======
    path('', index, name='index'),
>>>>>>> Stashed changes
]