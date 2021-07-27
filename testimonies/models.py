from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Testimony(models.Model):
    testimonial_name = models.CharField(max_length=300)
    position = models.CharField(max_length=250)
    body = models.TextField(blank=False, null=True)
    testimonial_photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')

    is_published = models.BooleanField(default=True)
    posted_date = models.DateTimeField(auto_now_add=True)



    def __str__ (self):
        return self.testimonial_name