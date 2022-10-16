from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.
class User(AbstractUser):
    pass

class CustomEmail(models.Model):
    recipient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    to_email_address = models.CharField(max_length=30)
    from_name = models.TextField()
    from_email = models.TextField()
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(null=True,upload_to="")