from django.urls import path
from . import views
app_name = "myapp"
urlpatterns = [
	path("", views.home, name="home"),
	path("add-task/", views.addTask, name="add-task"),
	path("pending/", views.pending, name="pending-tasks"),
	path("done/", views.done, name="completed-tasks"),
]