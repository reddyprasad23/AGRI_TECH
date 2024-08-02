from django.urls import path
from . import views
from django.contrib.auth import views as v
urlpatterns =[
path('',views.first,name="first"),
path('home/',views.home,name="home"),
path('about/',views.about,name="about"),
path('contact/',views.contact,name="contact"),
path('logout/',v.LogoutView.as_view(template_name="agritech/logout.html"),name="logout"),
path('register/',views.register,name="register"),
path('login/',v.LoginView.as_view(template_name="agritech/login.html"),name="login"),
path('profile/',views.farmerdetail,name="profile"),
path('cprofile/',views.cprofile,name="cprofile"),
path('farmerlist/',views.farmerslist,name="farmerlist"),
path('buyerlist/',views.buyerlist,name="buyerlist"),
path('orders/',views.orders,name="orders"),
path('userprofile/',views.userprofile,name="userprofile"),
path('displayorders/',views.displayorders,name="dorders"),
path('update/',views.updatedata,name="update")
]