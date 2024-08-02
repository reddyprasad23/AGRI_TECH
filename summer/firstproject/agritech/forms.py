from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import User
from . models import FarmerTable,ConsumerTable,OrdersTable

class Userform(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=["username"]
		widgets={"username":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Username"})}
class FarmerForm(forms.ModelForm):
	class Meta:
		model=FarmerTable
		fields=["village","district","state","mobile","land","crops","price","image"]
		widgets={
		"village":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Village Name"}),
		"district":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter district Name"}),
		"state":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter state Name"}),
		"mobile":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter mobile Number"}),
		"land":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"land in acres"}),
		"crops":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"crop grown"}),
		"price":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"price of product(in quintal)"}),
		}
class UpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","email"]
		widgets = {
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mail Id",
			}),
		}


class ConsumerForm(forms.ModelForm):
	class Meta:
		model = ConsumerTable
		fields = ["phonenumber","state","idproof","requiredproduct","quantity","image"]
		widgets = {
		"phonenumber":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter PhoneNumber"
			}),
		"state":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter state"
			}),
		"idproof":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter idnumber",
			}),
		"requiredproduct":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter required product",
			}),
		"quantity":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Quantity required",
			}),
		}
class Orderform(forms.ModelForm):
	class Meta:
		model=OrdersTable
		fields=['cropname','requantity','advanceamount']
		widgets={
		"cropname":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Product Name"}),
		"requantity":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Required Quantity"}),
		"advanceamount":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Advance Amount(25%)"}),
		}

