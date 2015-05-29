from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
#from .forms import *

# Register your models here.

class MyUserAdmin(UserAdmin):
    list_display = ('username','get_full_name','email','is_staff','is_active','gender')
    fieldsets = (
            ('User Info',{'fields':(('username','email'),'password')}),
            ('Permissions',{'fields':('is_active','is_staff','is_superuser')}),
            ('Personal Info',{'fields':(('first_name','last_name'),('gender','dob'))}),
            ('Important Dates',{'fields':('last_login','date_joined')}),
          )
    add_fieldsets=(
               ('Add User',{'fields':('username','email','first_name','last_name','gender')}),
             )
admin.site.register(BetitUser,MyUserAdmin)
admin.site.register(UserProfile)
admin.site.register(hashTags)
admin.site.register(Photo)
admin.site.register(Workplace)
