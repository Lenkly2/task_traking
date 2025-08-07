from django.urls import path
from .views import ProjectListView

urlpatterns = [
    # path("", index, name='home'),
    path("project_list/",ProjectListView.as_view(),name='project_list'),

]
