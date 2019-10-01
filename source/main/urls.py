"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, TaskView, Task_create_view, Task_edit_view, Task_delete_view, StatusView,TypeView, \
    Status_create_view, Type_create_view, Status_delete_view, Type_delete_view, Status_edit_view, Type_edit_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/create/', Task_create_view.as_view(), name='create_task'),
    path('task/delete/<int:pk>/', Task_delete_view.as_view(), name='delete_task'),
    path('task/update/<int:pk>/', Task_edit_view.as_view(), name='update_task'),
    path('status/', StatusView.as_view(), name='status_view'),
    path('type/', TypeView.as_view(), name='type_view'),
    path('status/add', Status_create_view.as_view(), name='create_status'),
    path('type/add', Type_create_view.as_view(), name='create_type'),
    path('status/delete/<int:pk>/', Status_delete_view.as_view(), name='delete_status'),
    path('type/delete/<int:pk>/', Type_delete_view.as_view(), name='delete_type'),
    path('status/update/<int:pk>/', Status_edit_view.as_view(), name='status_update'),
    path('type/update/<int:pk>/', Type_edit_view.as_view(), name='type_update'),

]
