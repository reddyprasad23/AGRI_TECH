from django.shortcuts import render,redirect
from .forms import Userform,FarmerForm,UpdateForm,ConsumerForm,Orderform
from .models import User,FarmerTable,ConsumerTable,OrdersTable
from django.contrib import messages

# Create your views here.
def first(request):
	return render(request,'agritech/firstpage.html')

def home(request):
	return render(request,'agritech/home.html')

def about(request):
	return render(request,'agritech/about.html')

def contact(request):
	return render(request,'agritech/contact.html')

def logout(request):
	if request.method == 'POST':
		return render(request,'agritech/logout.html')

def register(request):
	if request.method == 'POST':
		g=Userform(request.POST)
		if g.is_valid():
			g.save()
			return redirect('/profile/')
	g=Userform()
	return render(request,'agritech/register.html',{'a':g})

def farmerdetail(request):
	w = User.objects.get(id=User.objects.last().id)
	if request.method == "POST":
		t = FarmerForm(request.POST,request.FILES)
		y = UpdateForm(request.POST,instance=w)
		if t.is_valid() and y.is_valid():
			k = t.save(commit = False)
			k.usd_id = w.id
			w.farmer = 1
			w.save()
			y.save()
			k.save()
			return redirect('/login/')
	t = FarmerForm()
	y = UpdateForm(instance  = w)
	return render(request,'agritech/profile.html',{'q':y,'r':t})

def cprofile(request):
	w = User.objects.get(id=User.objects.last().id)
	if request.method == "POST":
		t = ConsumerForm(request.POST,request.FILES)
		y = UpdateForm(request.POST,instance=w)
		if t.is_valid() and y.is_valid():
			k = t.save(commit = False)
			k.usc_id = w.id
			w.buyer = 1
			w.save()
			y.save()
			k.save()
			return redirect('/login/')
	t = ConsumerForm()
	y = UpdateForm(instance  = w)
	return render(request,'agritech/cprofile.html',{'q':y,'r':t})


def farmerslist(request):
	k=User.objects.all()
	f={}
	for i in k:
		#t=FarmerTable.objects.get(usd_id=2)
		if i.farmer==1:
			t=FarmerTable.objects.get(usd_id=i.id)
			f[i.id]=i.username,t.mobile,t.crops,t.price
	return render(request,'agritech/farmerlist.html',{'y':f.values()})


def buyerlist(request):
	c={}
	k=User.objects.all()
	for i in k:
		if i.buyer==1:
			t=ConsumerTable.objects.get(usc_id=i.id)
			c[i.id]=i.username,t.phonenumber,t.requiredproduct,t.state
	return render(request,'agritech/buyerlist.html',{'y':c.values()})

def userprofile(request):
	n=request.user.id
	l=[]
	if request.user.farmer == 1:
		m=FarmerTable.objects.get(usd_id=n)
		l=[request.user.username,request.user.email,m.mobile,m.village,m.district,m.state,m.crops,m.land,m.image]
		return render(request,'agritech/farmerprofile.html',{'k':l})
	elif request.user.buyer == 1:
		m=ConsumerTable.objects.get(usc_id=n)
		l=[request.user.username,request.user.email,m.phonenumber,m.state,m.idproof,m.requiredproduct,m.image]
		return render(request,'agritech/consumerprofile.html',{'k':l})
	
def orders(request):
	if request.method == 'POST':
		g=Orderform(request.POST)
		if g.is_valid():
			l=g.save(commit=False)
			l.uso_id=request.user.id
			l.save()
			h=g.save(commit=False)
			h.buyername=request.user.username
			h.save()
			g.save()
			return redirect('/farmerlist/')
	g=Orderform()
	return render(request,'agritech/order.html',{'a':g})

def displayorders(request):
	n=request.user.id
	k=OrdersTable.objects.all()
	l={}
	j=0
	for i in k:
		if n==i.uso_id:
			l[j]=i.cropname,i.requantity,i.advanceamount
		j+=1
	#print(l)
	return render(request,'agritech/dorders.html',{'q':l.values()})
def updatedata(request):
	k=request.user
	content={}
	a=UpdateForm(instance=k)
	if request.user.buyer == 1:
		h=ConsumerTable.objects.get(usc=k)
		if request.method == 'POST':
			g=ConsumerForm(request.POST,request.FILES,instance=h)
			if g.is_valid():
				a=User.objects.get(id=k.id)
				a.save()
				g.save()
				a.update({'first_name':k.first_name,'last_name':k.last_name,'email':k.email})
				a.save()
				return redirect('/home/')
		form=ConsumerForm(instance=h)
		content['form']=a,form
		return render(request,'agritech/update.html',content)
	elif request.user.farmer == 1:
		h=FarmerTable.objects.get(usd=k)
		if request.method == 'POST':
			g=FarmerForm(request.POST,request.FILES,instance=h)
			if g.is_valid():
				a=User.objects.get(id=k.id)
				a.save()
				g.save()
				a.update({'first_name':k.first_name,'last_name':k.last_name,'email':k.email})
				a.save()
				return redirect('/home/')
		form=FarmerForm(instance=h)
		content['form']=a,form
		return render(request,'agritech/update.html',content)
def email(request):
	form=register(request.POST)
	if form.is_valid():
		user.form.save()
		sub="Welcome to AGRI_TECH online trading"