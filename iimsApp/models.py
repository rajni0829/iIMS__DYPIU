from django.db import models
from django.contrib.auth.models import AbstractUser

# class CustomerUser(AbstractUser):
#     user_type_data = ((1,'Admin'),(2,'Faculty'),(3,'Students'))
#     usr_type = models.CharField(default=1,choices=user_type_data,max_length=10)
# Create your models here.
# class Admin(models.Model):
#     pass

class dept(models.Model):
    dept_id = models.CharField(primary_key=True,max_length=50)
    dept_name = models.CharField(max_length=50)
    objects=models.Manager()


# https://stackoverflow.com/questions/17523263/how-to-create-password-field-in-model-django
class faculty_details(models.Model):
    faculty_id = models.CharField(primary_key=True,max_length=255)
    faculty_name = models.CharField(max_length=255)
    faculty_email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    faculty_rn = models.CharField(max_length=100)
    availability = models.BooleanField()
    objects = models.Manager()


class classroom(models.Model):
    room_no =  models.CharField(primary_key=True,max_length=255)
    # room_no =  models.IntegerField(primary_key=True,max_length=255)    
    status = models.CharField(max_length=255)
    course_id = models.CharField(max_length=255)
    capacity = models.IntegerField(blank=True)
    projector = models.IntegerField(blank=True)
    ac = models.IntegerField(blank=True)
    computer = models.IntegerField(blank=True)
    desks = models.IntegerField(blank=True)
    whiteboard = models.IntegerField(blank=True)
    count = models.IntegerField(blank=True)
    type = models.CharField(max_length=255)
    objects = models.Manager()

class course(models.Model):
    course_id = models.CharField(primary_key=True,max_length=255)
    faculty_id = models.ForeignKey(faculty_details,on_delete=models.CASCADE,max_length=255)
    course_fullname = models.CharField(max_length=255)
    course_shortname = models.CharField(max_length=255)
    room_no =  models.CharField(max_length=255)
    semester = models.IntegerField(blank=True)
    objects = models.Manager()



class faculty_tt(models.Model):
    faculty_id = models.CharField(primary_key=True,max_length=255)
    start_date = models.DateTimeField(auto_now_add = True)
    course_id = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    ta = models.CharField(max_length=255)
    objects = models.Manager()



class timetable_sem6(models.Model):
    start_date = models.DateTimeField(primary_key=True,auto_now_add = True)
    end_date = models.DateTimeField(auto_now_add = True)
    Monday = models.CharField(max_length=255)
    Tuesday = models.CharField(max_length=255)
    Wednesday = models.CharField(max_length=255)
    Thursday = models.CharField(max_length=255)
    Friday = models.CharField(max_length=255)
    Saturday= models.CharField(max_length=255)
    objects = models.Manager()


class students_2019(models.Model):
    prn = models.CharField(primary_key=True,max_length=255)
    student_name = models.CharField(max_length=255)
    student_email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    student_phone = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    track = models.CharField(max_length=255)
    year = models.IntegerField()
    objects = models.Manager()
    

class exam(models.Model):
    exam_id = models.CharField(primary_key=True,max_length=255)
    faculty_id = models.ForeignKey(faculty_details,on_delete=models.CASCADE,max_length=255)
    room_no =  models.ForeignKey(classroom,on_delete=models.DO_NOTHING,max_length=255)
    room_no =  models.ForeignKey(classroom,on_delete=models.DO_NOTHING,max_length=255)
    exam_name = models.CharField(max_length=255)
    course_id = models.ForeignKey(course,on_delete=models.CASCADE,max_length=255)
    start_date = models.DateTimeField(auto_now_add = True)
    end_date = models.DateTimeField(auto_now_add = True) 
    exam_type = models.CharField(max_length=255)
    prn = models.ForeignKey(students_2019,on_delete=models.CASCADE,max_length=255)
    objects = models.Manager()

