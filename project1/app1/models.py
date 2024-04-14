from django.db import models

class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=15)

    def _str_(self):
        return self.name

class Task(models.Model):
    TASK_TYPE_CHOICES=[
        ('Pending','Pending'),
        ('Done','Done'),
    ]

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task_detail=models.TextField()
    task_type=models.CharField(max_length=10,choices=TASK_TYPE_CHOICES)

    def _str_(self):
        return self.task_detail