from django.db import models

class Blog(models.Model):
    header = models.CharField(max_length=255)
    content = models.TextField()
    img_content = models.ImageField()