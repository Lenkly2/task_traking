from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LogoutView, LoginView
from .models import Project, Task, Comment
from .forms import TaskForm, ProjectForm, CommentForm
# Create your views here.

class MainView(TemplateView):
    template_name = "task_traking/index.html"

class ProjectListView(ListView):
    model = Project
    template_name = "task_traking/projectlist.html"
    context_object_name = "projectlist"

class TaskListView(ListView):
    model = Task
    template_name = "task_traking/tasklist.html"
    context_object_name = "tasklist"

    def get_queryset(self):
        project = self.kwargs["pk"]
        return Task.objects.filter(project=project)

class TaskDetailView(DetailView):
    model = Task
    template_name = "task_traking/detailtask.html"
    context_object_name = "detailtask"


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_traking/taskcreate.html"
    success_url = "./"
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "task_traking/projectcreate.html"
    success_url = "../"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class CreateCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "task_traking/comentcreate.html"
    succes_url = "../"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RegisterView(FormView):
    template_name = "auth/register.html"
    form_class = UserCreationForm
    success_url = "../"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    success_url = "../"

class CustomLogoutView(LogoutView):
    next_page = "login"