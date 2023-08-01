from django.db import models

from django.contrib.auth.models import AbstractUser 
from django.utils.text import slugify

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
        


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='profile_images/',default = 'def.jpg',blank=True,null=True)
    dob = models.DateTimeField(blank=True,null=True)
    slug = models.SlugField(unique=True,max_length=255,blank=True) 

    created = models.DateTimeField(auto_now_add=True) 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username) 
            super(Profile, self).save(*args, **kwargs)
            
    def __str__(self):
        return f"{self.user.first_name}"