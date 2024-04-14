from django.urls import path
from . import views

urlpatterns = [

    path('add_user/',views.add_user,name='add_user'),
    path('add_task/',views.add_task,name='add_task'),
    path('list_users/',views.list_users,name='list_users'),
    path('list_tasks/',views.list_tasks,name='list_tasks'),
    path('export_to_excel/',views.export_to_excel,name='export_to_excel')
]