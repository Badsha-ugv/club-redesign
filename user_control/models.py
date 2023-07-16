from django.db import models

from django.contrib.auth.models import AbstractUser 

USERS_TYPE = (
    ('admin','admin'),
    ('teams','team'),
    ('student','student'),
)
SEMESTER = (
    ('1','1st '),
    ('2','2nd'),
    ('3','3rd'),
    ('4','4th'),
    ('5','5th'),
    ('6','6th'),
    ('7','7th'),
    ('8','8th'),
)

class User(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USERS_TYPE,blank=True) 
    phone = models.CharField(max_length=15, blank=True) 
    # image = models.ImageField(upload_to='user_images/', blank=True) 
    student_id = models.CharField(max_length=20,unique=True) 
    semester = models.CharField(max_length=1, choices=SEMESTER, blank=True) 
    section = models.CharField(max_length=5, blank=True) 
    department = models.CharField(max_length=50, blank=True)


    created  = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} {self.semester}" 
    
    class Meta:
        verbose_name = 'User Account'
        
