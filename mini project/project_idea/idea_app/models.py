
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User




class Modelsuper(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        abstract=True
        
class Course(Modelsuper):
    course=models.CharField(max_length=300)
    def __str__(self):
        return self.course
    
    
class Tech(Modelsuper):
    Tech=models.CharField(max_length=300)
    def __str__(self):
        return self.Tech
    
    
class Syllabus(Modelsuper):
    Syllabus=models.CharField(max_length=255)
    def __str__(self):
        return self.Syllabus


Project_Type_CHOICES = [
    ('main_project', 'Main Project'),
    ('mini_project', 'Mini Project'),
    ('class_project', 'Class Project'),
    ]
    
class ProjectDetails(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE)
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    Project_type = models.CharField(max_length=100,choices=Project_Type_CHOICES)
    Title_of_theproject = models.CharField(max_length=100)
    Description= models.CharField(max_length=300)
    






    




    
    
    
    

    