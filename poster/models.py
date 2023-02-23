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
    color = models.CharField(max_length=200, blank=True)
    dimensions = models.CharField(max_length=300, blank=True)
    cost = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    ORIGINAL = 'OR'
    NEWER = 'NE'
    VERY_GOOD = 'VG'
    GOOD = 'GD'
    FAIR = 'FR'
    CONDITION_CHOICES = [
        (ORIGINAL, 'Never Worn, with Original Tags'),
        (NEWER, 'Never Worn'),
        (VERY_GOOD, 'Very Good Condition'),
        (GOOD, 'Good Condition'),
        (FAIR, 'Fair Condition'),
    ]
    condition = models.CharField(
        max_length=2,
        choices=CONDITION_CHOICES,
        default=GOOD,
    )
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def is_upperclass(self):
        return self.condition in {self.VERY_GOOD, self.GOOD}

    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE,
                                related_name="posts")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.name
