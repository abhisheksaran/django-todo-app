from django.urls import path
from . import views
app_name = "myapp"
urlpatterns = [
	path("", views.home, name="home"),
	path("add-task/", views.addTask, name="add-task"),
	path("pending/", views.pending, name="pending-tasks"),
	path("done/", views.done, name="completed-tasks"),
	path("delete/(?P<pk>[0-9]+)$", views.delete, name="delete-task"),
	path("mark-pending/(?P<pk>[0-9]+)$", views.markPending, name="mark-pending"),
	path("mark-done/(?P<pk>[0-9]+)$", views.markDone, name="mark-done"),
]