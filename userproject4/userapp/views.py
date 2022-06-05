from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userapp.forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.
def menu_view(request):
	return render(request,'userapp/menu.html')

def home_view(request):
	return render(request,'userapp/home.html')

def javaexams_view(request):
	return render(request,'userapp/javaexams.html')
@login_required
def pythonexams_view(request):
	return render(request,'userapp/pythonexams.html')

def logout_view(request):
	return render(request,'userapp/logout.html')

def signup_view(request):
	forms = SignUpForm()
	if request.method == 'POST':
		forms = SignUpForm(request.POST)
		user = forms.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request,'userapp/signup.html',{'form':forms})