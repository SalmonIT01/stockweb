from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Details,Unit
# from function import*
# Create your views here.

def index(request):
    from django.core import serializers
    data = serializers.serialize("python",Details.objects.all().select_related('unit'))
    
    unit_data = Details.objects.all().select_related('unit')

    context = {
        'data': unit_data, }

    return render(request, 'app_home/index.html', context)

def home(request):
    from django.core import serializers
    
    unit_data = Details.objects.select_related('unit').values('product_id', 'product_name', 'unit__unit_name', 'amount', 'status_id')
    
    context = {'dataUnit':unit_data,}

    return render(request, 'app_home/home.html', context)


# def showdb():
#     db = '''SELECT * 
#             FROM products2; '''
#     cursur.execute(db)
#     product_table = cursur.fetchall()
#     print(product_table)


