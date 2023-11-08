from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Details,Unit
# from function import*
# Create your views here.
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



# def showdb():
#     db = '''SELECT * 
#             FROM products2; '''
#     cursur.execute(db)
#     product_table = cursur.fetchall()
#     print(product_table)


