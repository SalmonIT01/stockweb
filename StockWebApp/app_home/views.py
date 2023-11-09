from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Details,Unit
# from function import*
# Create your views here.
def home(request):
    return render(request,'app_home/home.html')
def index(request):
    from django.core import serializers
    data = serializers.serialize("python",Details.objects.all())

    context = {
        'data': data,

    }

    return render(request, 'app_home/index.html', context)



# def showdb():
#     db = '''SELECT * 
#             FROM products2; '''
#     cursur.execute(db)
#     product_table = cursur.fetchall()
#     print(product_table)


