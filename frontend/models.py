from django.db import models
from user_control.models import User 
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField



# Create your models here.

RATING = (
    ('1','1'),
    ('3','2'),
    ('2','3'),
)


class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True) 

    def __str__(self):
        return str(self.name) 

class Subcategory(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) 

class Project(models.Model):
    # user
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = RichTextField()
    image = models.ImageField(upload_to= 'project_images/', blank=True, null=True) 
    source = models.CharField(max_length=400,blank=True, null=True)
    rating = models.CharField(max_length=1, choices=RATING, null=True, blank=True) 

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title) 
    

class Blog(models.Model):
    # user
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = RichTextField()
    image = models.ImageField(upload_to='blog_images/', blank=True,null=True) 
    rating = models.CharField(max_length=1, choices=RATING, null=True, blank=True) 

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.created}" 
    



class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=400,blank=True, default="No Title")
    desc = RichTextField()
    source_code = models.CharField(max_length=220,blank=True) 
    video_url = models.CharField(max_length=220,blank=True) 
    resource_link = models.CharField(max_length=220,blank=True) 
    
    slug =models.SlugField(max_length=300)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Project, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.title}"


class SliderImage(models.Model):
    image  = models.ImageField(upload_to='slider_image/',blank=True, null=True) 

    def __str__(self):
        return f"{self.id}"
