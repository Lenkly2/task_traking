from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Project
# Create your views here.

class ProjectListView(ListView):
    model = Project
    template_name = "task_traking/Projectlist.html"
    context_object_name = "projectlist"
