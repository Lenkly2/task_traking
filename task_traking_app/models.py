from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Member(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

class Project(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

class Task(models.Model):
    STATUS_CHOISES = [
        ("todo", "To Do"),
        ("in_progress","In Progress"),
        ("done","Done"),
    ]

    PRIORITY_CHOISES = [
        ("low","Low"),
        ("medium","Medium"),
        ("high","High"),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOISES, default="todo")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOISES, default="low")
    due_date = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

class Comment(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
