from django.db import models
from .validators import validate_file_extension


class Post(models.Model):
    cover = models.FileField(upload_to='file', validators=[validate_file_extension])

    # def __str__(self):
    #   return self.cover

    class Meta:
        ordering = ['cover']


class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=150, unique=True)
    profile = models.TextField()

    def __str__(self):
        return self.name
