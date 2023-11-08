from django.http.response import HttpResponse
from django.shortcuts import render
# from function import*



# Create your views here.
def home(request):
    return render(request,'app_home/home.html')

# def showdb():
#     db = '''SELECT * 
#             FROM products2; '''
#     cursur.execute(db)
#     product_table = cursur.fetchall()
#     print(product_table)


#Fjkblnlufk
#hjkuhihogdtgljnuilbkujh