from django.db import models
from users.models import CustomUser


# Create your models here.

CATEGORY_CHOICES = (
    ('Breaking', "Breaking"),
    ('Entertainment', 'Entertainment'),
    ('Politics', 'Politics'),
    ('Sports', 'Sports'),
    ('Crypto', 'Crypto'),
    ('General', 'General'),
    ('Business', "Business"),
    ('Science', "Science"),
    ('Health', "Health"),
    ('Technology', "Technology"),
)

options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


class News(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    content = models.TextField()
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default='General')
    image = models.ImageField(upload_to='news_images')
    other_image = models.ImageField(
        upload_to='other_images', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=options, default='published')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_posted',)
        verbose_name_plural = 'News'


class Category(models.Model):
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images")
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self) -> str:
        return self.title


class Subscribers(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
