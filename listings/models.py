from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField
from PIL import Image
import os


            
         

class Listing(models.Model):
    name = models.CharField(max_length=150, default=True)
    category = models.CharField(max_length=255)
    email = models.EmailField(max_length=150, blank=True)
    description = RichTextField(blank=True, null=True)
    photo_main = models.ImageField(upload_to = 'photos_main')
    photo_1 = models.ImageField(upload_to = 'photos_sub', blank=True)
    photo_2 = models.ImageField(upload_to = 'photos_sub', blank=True)
    photo_3 = models.ImageField(upload_to = 'photos_sub', blank=True)
    photo_4 = models.ImageField(upload_to = 'photos_sub', blank=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    phone_number =  models.CharField(max_length=11, blank=True, null=True)
    
    website =  models.CharField(max_length=150, blank=True)
    facebook =  models.CharField(max_length=150, blank=True)
    instagram =  models.CharField(max_length=150, blank=True)
    opening_time =  models.CharField(max_length=7, blank=True, null=True)
    closing_time =  models.CharField(max_length=7, blank=True, null=True)
    is_published = models.BooleanField(default=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=True)
    
    
    class Meta:
        ordering: ['-date']
 
    def __str__ (self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='photos_icons')
    
    
    class  Meta:
        verbose_name_plural = 'Categories'
    

    def __str__ (self):
        return self.name
    