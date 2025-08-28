from django.urls import path
from .views import ProjectListView, MainView, RegisterView,CreateTaskView, CreateProjectView,CustomLoginView, TaskListView,CustomLogoutView, TaskDetailView, CreateCommentView

urlpatterns = [
    path("", MainView.as_view(), name='home'),
    path("project_list/",ProjectListView.as_view(),name='project_list'),
    path("<int:pk>/",TaskListView.as_view(),name='task_list'),
    path("<int:pk>/details/",TaskDetailView.as_view(),name='task_detail'),
    path("create_task/",CreateTaskView.as_view(),name='create_task'),
    path("<int:pk>/details/create_comment/",CreateCommentView.as_view(),name='create_comment'),
    path("create_project/",CreateProjectView.as_view(),name='create_project'),
    path("register/",RegisterView.as_view(),name='register'),
    path("login/",CustomLoginView.as_view(),name='login'),
    path("logout/",CustomLogoutView.as_view(),name='logout'),

]
