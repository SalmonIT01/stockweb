from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Details,Unit
from django.core import serializers

# from function import*
# Create your views here.
def home(request):
    return render(request,'app_home/home.html')

def index(request):
    if "insert" in request.POST:
        product_id = request.POST.copy().get('product_id')
        product_name = request.POST.copy().get('product_name')
        unit_id = request.POST.copy().get('unit_id')
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
    
    data = serializers.serialize("python",Details.objects.all())
    context = {
            'data': data,
        }
    if "search" in request.POST:
        return redirect('search')
    return render(request, 'app_home/index.html', context)
    

def search(request):
    if "search" in request.POST:
        product_id_search =  request.POST.copy().get('product_id_search')
        data = serializers.serialize("python",Details.objects.filter(product_id__contains = product_id_search))
        context = {
            'data': data,
        }
        return render(request, 'app_home/search.html',context)
    if "insert" in request.POST:
        return redirect("index")
    return render(request, 'app_home/search.html')
    

    



# def showdb():
#     db = '''SELECT * 
#             FROM products2; '''
#     cursur.execute(db)
#     product_table = cursur.fetchall()
#     print(product_table)


