from django import forms
from .models import Task, Project

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date","updated_at","created_at","project"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "rows": 100}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "priority": forms.Select(attrs={"class": "form-select"}),
            "due_date": forms.DateTimeInput(attrs={"class": "form-select","type": "datetime-local"}),
            "updated_at": forms.DateTimeInput(attrs={"class": "form-select","type": "datetime-local"}),
            "created_at": forms.DateTimeInput(attrs={"class": "form-select","type": "datetime-local"}),
            "project": forms.Select(attrs={"class": "form-select"})
        }
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name","description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "rows": 100}),
            "description": forms.TextInput(attrs={"class": "form-control"})
        }