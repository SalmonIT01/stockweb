from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.home,name='home'),
    path('search',views.search,name='search'),
    path('borrow',views.borrow,name='borrow'),
    path('delete/<product_id>',views.delete,name='delete'),
    path('borrow/<product_id>',views.borrow,name='borrow'),
    path('update/<product_id>',views.update,name='update')
  
]