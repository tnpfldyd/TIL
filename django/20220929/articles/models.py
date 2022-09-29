from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length = 80)