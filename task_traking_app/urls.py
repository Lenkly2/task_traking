from django.urls import path
from .views import ProjectListView, MainView, RegisterView,CreateTaskView, CreateProjectView,LoginView, TaskListView

urlpatterns = [
    path("", MainView.as_view(), name='home'),
    path("project_list/",ProjectListView.as_view(),name='project_list'),
    path("<int:pk>/",TaskListView.as_view(),name='task_list'),
    path("create_task/",CreateTaskView.as_view(),name='create_task'),
    path("create_project/",CreateProjectView.as_view(),name='create_project'),
    path("register/",RegisterView.as_view(),name='register'),
    path("login/",LoginView.as_view(),name='login'),

]
