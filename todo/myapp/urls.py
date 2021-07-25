from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("pending/", views.pending, name="pending-tasks"),
	path("done/", views.done, name="completed-tasks"),
]