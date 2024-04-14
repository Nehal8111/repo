from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import UserForm,TaskForm
from .models import User,Task
import datetime

def add_user(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form=UserForm()
    return render(request,'add_user.html',{'form':form})

def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    else:
        form=TaskForm()
    return render(request,'add_task.html',{'form': form})

def list_users(request):
    users=User.objects.all()
    paginator=Paginator(users,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'list_users.html',{'page_obj': page_obj})

def list_tasks(request):
    tasks=Task.objects.all()
    paginator=Paginator(tasks,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'list_tasks.html',{'page_obj': page_obj})

def export_to_excel(request):
    wb=openpyxl.Workbook()
    ws_users=wb.activeq
    ws_users.title="Users"
    ws_tasks=wb.create_sheet(title="Tasks")

    ws_users.append(["ID","Name","Email","Mobile"])
    ws_tasks.append(["ID","User","Task Detail","Task Type"])

    users=User.objects.all()
    for user in users:
        ws_users.append([user.id,user.name,user.email,user.mobile])
    tasks=Task.objects.all()
    for task in tasks:
        ws_tasks.append([task.id,task.user.name,task.task_detail,task.task_type])

    response=HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition']=f'attachment; filename=export_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.xlsx'
    wb.save(response)
    return  response

