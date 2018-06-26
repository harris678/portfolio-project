from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField(auto_now=False)
    body = models.TextField()
    summary = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to = 'images/')
