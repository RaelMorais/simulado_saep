from django.db import models

# User model class 
class User(models.Model):
    name = models.CharField(max_length=255, default=' ')
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255, default='')


# Task model for to-do 
class Task(models.Model):
    description = models.CharField(max_length=255)
    name_class = models.CharField(max_length=255)
    priority = models.CharField(choices=(('high', 'high'), ('mid', 'mid'), ('low', 'low')), max_length=5, default='low')
    register_date = models.DateField()
    status = models.CharField(choices=(("todo", "To Do"),("in_progress", "In Progress"),("done", "Done")), max_length=25, default="todo")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Create your models here.
