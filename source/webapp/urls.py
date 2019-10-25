from django.urls import path
from webapp.views import IndexView, TaskView, TaskCreateView, TaskEditView, TaskDeleteView, StatusView,TypeView, \
    StatusCreateView, TypeCreateView, StatusDeleteView, TypeDeleteView, StatusEditView, TypeEditView, ProjectsView, ProjectView, \
    ProjectEditView, ProjectDeleteView, ProjectCreateView, TaskForProjectsCreateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/create/', TaskCreateView.as_view(), name='create_task'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    path('task/update/<int:pk>/', TaskEditView.as_view(), name='update_task'),
    path('status/', StatusView.as_view(), name='status_view'),
    path('type/', TypeView.as_view(), name='type_view'),
    path('status/add', StatusCreateView.as_view(), name='create_status'),
    path('type/add', TypeCreateView.as_view(), name='create_type'),
    path('status/delete/<int:pk>/', StatusDeleteView.as_view(), name='delete_status'),
    path('type/delete/<int:pk>/', TypeDeleteView.as_view(), name='delete_type'),
    path('status/update/<int:pk>/', StatusEditView.as_view(), name='status_update'),
    path('type/update/<int:pk>/', TypeEditView.as_view(), name='type_update'),
    path('projects/', ProjectsView.as_view(), name='view_projects'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/create/', ProjectCreateView.as_view(), name='create_project'),
    path('project/delete/<int:pk>/', ProjectDeleteView.as_view(), name='delete_project'),
    path('project/update/<int:pk>/', ProjectEditView.as_view(), name='update_project'),
    path('project/<int:pk>/add-task/',TaskForProjectsCreateView.as_view(), name='project_task_create'),
]