from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import*
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email','first_name','last_name']
 
