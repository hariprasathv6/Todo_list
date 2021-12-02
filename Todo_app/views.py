from django.shortcuts import render,redirect
from django.http import HttpResponse
from .import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TasksForm,SignUpForm
from .models import Des

# Create your views here.

@login_required(login_url='login')
def base(request):



	return render(request,"base.html")


def sign_up(request):

	form = SignUpForm()
	if request.method == 'POST':
		form = SignUpForm(request.POST)	
		if form.is_valid():

			form.save()

			messages.info(request,'Your account was created successfully lets Login')
			
			
		else:
			form=SignUpForm()
	return render(request,'Authenticate/sign_up.html',{'form':form})





def login_user(request):
	if request.user.is_authenticated:
		return redirect('/task')

	else:
		if request.method == "POST":
			username = request.POST["username"]
			password = request.POST["password"]
			user = authenticate(request,username = username,password = password)



			if user is not None:
				login(request,user)
				return redirect('/task')

			else:
			    messages.info(request,'Username or Password is incorrect')


	return render(request,'Authenticate/login.html')

	

def logout_user(request):
	logout(request)

	return redirect('/login')




@login_required(login_url='login')
def tasks(request):
	des = Des.objects.filter(user=request.user)

	
	

	return render(request,'task.html',{'des':des})



def delete(request,id):
	des = Des.objects.get(id=id)
	des.delete()

	return redirect('/task')


			

def update(request,id):
    des = Des.objects.get(id=id)
    if request.method =='POST':
        form = TasksForm(request.POST,instance=des) #update on old data use instance

 

        if form.is_valid():
            form.save()
            return redirect('/task')

    return render(request,'update.html',{'form':des})
    








@login_required(login_url='login')
def add(request):
	form = TasksForm()
	if request.method == 'POST':
		form = TasksForm(request.POST)
		if form.is_valid():
			fs =form.save()	
			fs.user = request.user
			fs.save()
			return redirect('/task')




	return render(request,'add.html',{'form':form})







