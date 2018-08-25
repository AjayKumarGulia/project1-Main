from django.db import models

class blog(models.Model):
    Title = models.CharField(max_length = 100)
    Post_date = models.DateTimeField()
    blog_body = models.TextField()
    image = models.ImageField(upload_to='images/')
