from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Userinfo(models.Model):
    user = models.CharField(max_length=20, db_column="user",default="JohnDoe", verbose_name='Username')
    user_id = models.CharField(max_length=8, default=18201000, verbose_name='User ID', unique=True)
    user_firstname = models.CharField(max_length=20, db_column="First name",default="John", verbose_name='First Name')
    user_lastname = models.CharField(max_length=20, db_column="Last name", default="Doe", verbose_name='Last Name')
    user_semester = models.CharField(max_length=50, db_column="Semester", default = "1-1", verbose_name='Semester')

    class Meta:
        db_table = "User Info"

class Courseinfo(models.Model):
    course_userid = models.CharField(max_length=8, default=18201000, verbose_name='User ID')
    course_semester = models.CharField(max_length=50, db_column="Semester", default = "1-1", verbose_name='Semester')
    course_id = models.CharField(max_length=7, db_column="Course ID", default="CSE 101", verbose_name='Course ID')
    course_title = models.CharField(max_length=50, db_column="Course Title", default="Computer Fundamentals", verbose_name='Course Title')

    class Meta:
        db_table = "Course Info"
