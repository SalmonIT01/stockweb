from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.home,name='home'),
    path('search',views.search,name='search'),
    path('delete/<product_id>',views.delete,name='delete'),
    path('update/<product_id>',views.update,name='update')
  
]