from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField




class NewsPost(models.Model):
    title = models.CharField(max_length=300, blank=False)
    category = models.CharField(max_length=200, default=True)
    body = models.TextField(blank=False)
    photo = models.ImageField(upload_to = 'Newsphotos/%Y/%m/%d/', default=True)
    date = models.DateField(auto_now_add=True)
    is_publish = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    