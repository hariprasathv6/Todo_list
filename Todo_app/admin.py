from django.contrib import admin
from .models import Des

# Register your models here.

class DesAdmin(admin.ModelAdmin):
	list = ['user','Tasks']

admin.site.register(Des,DesAdmin)


