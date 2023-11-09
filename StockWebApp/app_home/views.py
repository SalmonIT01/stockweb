from django.http.response import HttpResponse
<<<<<<< Updated upstream
from django.shortcuts import render
from .models import Details,Unit
# from function import*
# Create your views here.
=======
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.
def index(request):
    stock_items = StockItem.objects.all()
    return render(request, 'app_home/index.html', {'stock_items': stock_items})

>>>>>>> Stashed changes
def home(request):
    return render(request,'app_home/home.html')
def index(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        product_name = request.POST['product_name']
        unit_id = request.POST['unit_id']
        amount = request.POST['amount']
        status_id = request.POST['status_id']

        #Creating the Object of record every time user click on 'Add Deta'
        obj = Details()
        obj.product_id = product_id
        obj.product_name = product_name
        obj.save()

    from django.core import serializers
    data = serializers.serialize("python",Details.objects.all())

    context = {
        'data': data,

    }

    return render(request, 'app_home/index.html', context)



<<<<<<< Updated upstream
# def showdb():
#     db = '''SELECT * 
#             FROM products2; '''
#     cursur.execute(db)
#     product_table = cursur.fetchall()
#     print(product_table)


=======
 
>>>>>>> Stashed changes
