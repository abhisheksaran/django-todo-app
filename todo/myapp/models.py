from django.db import models

# Create your models here.


class Todo(models.Model):
	task_status = (
		("-1","pending"), ("1"="done"),
	)
	task = modles.CharField(max_length=99)
	deadline = models.DateTimeField()
	status = models.ChoiceField(choices = task_status,default="-1")

	def __str__(self):
		return f"Task:{self.task}, Deadline:{self.deadline}, Status:{self.status}"