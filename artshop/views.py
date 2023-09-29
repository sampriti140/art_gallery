from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import *
from .forms import *
# Create your views here.


def index(request):
    a=prod.objects.all()
    return render(request,'index.html',{'x':a})
def form(request):
    return render(request,'form.html')
def new(request):
    return render(request,'new.html')
def home(request):
    return render(request,'home.html')
def aboutus(request):
    return render(request,'about_us.html')
def contactus(request):
    return render(request,'contact_us.html')
def form1(request):
    return render(request,'form1.html')
def check(request,id):
    u=prod.objects.get(id=id)
    return render(request,'formnew.html',{'a':u})
   
    

def orders(request):
    a=formation()
    try:
        a.name=request.GET["name"]
        a.email=request.GET["email"]
        a.number=request.GET["number"]
        a.address=request.GET["address"]
        a.Artworks=request.GET["pname"]
        a.save()
    except:
        pass
    return render(request,'formnew.html')
def formnew(request):
   return render(request,'formnew.html')
    
   
# def form2(request,pname):
#     f = formation.objects.all()
#     # f1= f.objects.get(Artworks=pname)
#     data={

#     }
#     try:
#         f.name=request.GET["name"]
#         f.email=request.GET["email"]
#         f.number=request.GET["number"]
#         f.address=request.GET["address"]

#        # f.Productname=request.GET["Productname"]
#         # f.Artworks=request.GET["Artworks"]
#         f.save()
#     except:
#         pass
#     print('Artworks')
#     return render(request,'formnew.html')

def fom(request):
    return render(request,'formnew.html')
def contactuss(request):
    c=contact()
    try:
        c.name=request.GET["name"]
        c.email=request.GET["email"]
        c.message=request.GET["message"]
        c.save()
       
    except:
        pass
    return render(request,'contactuss.html')
def addpro(request):
    g = prod()
    try:
        g.pname=request.GET["name"]
        g.desc=request.GET["des"]
        g.price=request.GET["price"]
       
        g.save()
    except:
        pass
    # print('Artworks')
    return render(request,'addprod.html')

def shows(request):
    u = prod.objects.all()
    return render(request, 'shows.html',{'a':u})
def delet(request , id):
    u=prod.objects.get(id=id)
    u.delete()
    return redirect('../shows')
def edits(request , id):
    u= prod.objects.get(id=id)
    return render(request , 'edit.html',{'a':u})
def edcode(request , id):
    t= prod.objects.get(id=id)
    f= uform(request.GET, instance=t)
    if f.is_valid():
        f.save()
        return redirect('../shows')
    return render( request, 'edit.html',{'a':t})



def showorders(request):
    u= formation.objects.all()
    return render(request, 'showorders.html',{'a':u})

def dele(request , id):
    u=formation.objects.get(id=id)
    u.delete()
    return redirect('../showorders')
def editorders(request , id):
    u= formation.objects.get(id=id)
    return render(request , 'editorders.html',{'a':u})
def edcodes(request , id):
    t= formation.objects.get(id=id)
    f= dform(request.GET, instance=t)
    if f.is_valid():
        f.save()
        return redirect('../showorders')
    return render( request, 'editorders.html',{'a':t})

def adminlogin (request):
    return render(request,'adminlogin.html')
def Log_in(request):
    a= "ssaa"
    b= "1234"
    if a== "ssaa":
        # z= registration.objects.get(email=a)
        return render(request , 'welcome.html' )
    else:
        return render(request,'adminlogin.html')

