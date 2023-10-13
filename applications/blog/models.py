from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    date_time_created = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.CharField(blank=True, max_length=50)