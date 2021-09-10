from django.db import models


# Create your models here.
class Student_info(models.Model):
    student_name=models.CharField(max_length=20)
    email=models.EmailField()
    roll_number=models.IntegerField()
