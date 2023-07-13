from django.db import models

from django.contrib.auth.models import AbstractUser 

USERS_TYPE = (
    ('admin','admin'),
    ('teams','team'),
    ('student','student'),
)
SEMESTER = (
    ('1','1 '),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
)

class User(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USERS_TYPE,blank=True) 
    phone = models.CharField(max_length=15, blank=True) 
    image = models.ImageField(upload_to='user_images/', blank=True) 
    student_id = models.CharField(max_length=20, unique=True) 
    semester = models.CharField(max_length=1, choices=SEMESTER, blank=True) 
    section = models.CharField(max_length=5, blank=True) 

    created  = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} {self.semester}" 
    
    class Meta:
        verbose_name = 'User Account'
        
