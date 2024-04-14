from django.contrib import admin

# Register your models here.
from .models import User,Task

admin.register(User)
class user_admin(admin.ModelAdmin):
    list_display=('id','name','email','mobile')
    search_fields = ('name','email')     
      
admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','user','task_detail','task_type')
    list_filter = ('task_type','user')
    search_fields = ('task_detail','user__name')
