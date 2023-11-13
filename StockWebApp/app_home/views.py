import datetime
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import borrow_products,Unit,Details
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.contrib  import messages

# from function import*
# Create your views here.
def home(request):
    return render(request,'app_home/home.html')

def index(request):
    
    if "insert" in request.POST:
        product_id = request.POST.copy().get('product_id')
        product_name = request.POST.copy().get('product_name')
        unit_name = request.POST.copy().get('unit_name')
        unit_id = unit_convert (unit_name)
        amount = request.POST.copy().get('amount')
        status_id = request.POST.copy().get('status_id')
        print('test')
        #Creating the Object of record every time user click on 'Add Deta'
        obj = Details()
        obj.product_id = product_id
        obj.product_name = product_name
        obj.unit_id = unit_id
        obj.amount = amount
        obj.status_id = status_id
        obj.save()
    
    data = Details.objects.all().select_related('unit')
    context = {
            'data': data,
        }
    return render(request, 'app_home/index.html', context)
    

def search(request):
    if "search" in request.POST:
        try:
            product_id_search =  int(request.POST.copy().get('product_id_search'))
            data = Details.objects.filter(product_id__contains = product_id_search)
            context = {
                'data': data,
            }
            return render(request, 'app_home/search.html',context)
        except :
            product_id_search =  request.POST.copy().get('product_id_search')
            data = Details.objects.filter(product_name__contains = product_id_search)
            context = {
                'data': data,
            }
            return render(request, 'app_home/search.html',context)

    if "insert" in request.POST:
        return redirect("index")
    return render(request, 'app_home/search.html')


def delete (request,product_id):
    
    dele  = Details.objects.get(product_id=product_id)
    dele.delete()
    return redirect("index")

def unit_convert (unit_name_user):
    unit_con = Unit.objects.get(unit_name = unit_name_user)
    unit_num = unit_con.unit_id
    return unit_num

def borrow(request):
    now_time = datetime.datetime.now()
    if "borrow" in request.POST:
        product_id = request.POST.get('product_id')
        bproduct = id_convert (product_id)
        amount = request.POST.get('B_amount')
        now_time = datetime.datetime.now()
        
        obj = borrow_products()
        obj.bproduct_id = bproduct
        obj.borrow_date = now_time
        obj.b_amount = amount
        
        obj.save()
        
        context2 = {
        'b_productID' : Details.objects.filter(product_id=product_id),
        'b_amount'   : borrow_products.objects.filter(b_amount=amount),
        'nowtime2': now_time}
        data = borrow_products.objects.all().select_related('details')
    context = {
            'data': data,
        }
    return render(request, 'app_home/index.html', context)

def id_convert (bproduct_id):
    id_product = Details.objects.get(product_id = bproduct_id )
    id_con = id_product.id
    return id_con


    

    



# def showdb():
#     db = '''SELECT * 
#             FROM products2; '''
#     cursur.execute(db)
#     product_table = cursur.fetchall()
#     print(product_table)


