from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from Todo_app.models import Des

class SignUpForm(UserCreationForm):	
	class Meta:
		model = User
		fields = ['username','email','password1','password2']


class TasksForm(ModelForm):
	class Meta:
		model = Des
		fields =['Tasks']