from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_desc = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)
    completed= models.BooleanField(default=False)
    image = models.ImageField(upload_to="image/", default="image/None/Noimg.jpg")


    def __str__(self):
        return self.task_name
