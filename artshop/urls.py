from django.urls import path
from django import views
from . import views
urlpatterns=[
    path('index/', views.index),
    path('form/', views.form),
    path('new/', views.new),
    path('', views.home),
    path('aboutus/', views.aboutus),
    path('contactus/', views.contactus),
    path('form1/', views.form1),
    path('formnew/', views.formnew),
    path('check/<int:id>', views.check, name="check"),
    path('orders/', views.orders, name="orders"),

    path('Log_in',views.Log_in),
    path('adminlogin',views.adminlogin),
    
    path('contactuss/', views.contactuss),
    path('addpro/', views.addpro),
  
    
    path('shows' , views.shows),
    path('delet/<int:id>', views.delet),
    path('edits/<int:id>', views.edits),
    path('edcode/<int:id>', views.edcode),
    
    path('showorders' , views.showorders),
    path('dele/<int:id>', views.dele),
    path('editorders/<int:id>', views.editorders),
    path('edcodes/<int:id>', views.edcodes),
   
    ]
    