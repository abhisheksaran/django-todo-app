from django.db import models
from django_prometheus.models import ExportModelOperationsMixin
# Create your models here.


class Todo(ExportModelOperationsMixin('todo'), models.Model):
	task_status = (
		("pending","pending"), ("done","done"),
	)
	task = models.CharField(max_length=99)
	deadline = models.CharField(max_length=100)
	status = models.CharField(max_length=100, choices = task_status, default="pending")

	def __str__(self):
		return f"Task:{self.task}, Deadline:{self.deadline}, Status:{self.status}"

