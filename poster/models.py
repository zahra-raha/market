from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Not Sold"), (1, "Sold"))


class Category(models.Model):
    name = models.CharField(max_length=80)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="advertisement_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="categories")
    color = models.TextField()
    dimensions = models.TextField()
    cost = models.TextField()
    address = models.TextField()
    condition = models.TextField()
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

