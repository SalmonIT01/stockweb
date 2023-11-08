from django.urls import path
from . import views

urlpatterns = [
<<<<<<< Updated upstream
    path('',views.home,name='home')
    #k
=======
    path('',views.index,name="index"),
    path('home',views.home,name='home')
    
    
>>>>>>> Stashed changes
]