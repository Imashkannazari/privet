from django.db import models
from django.utils.text import slugify

class Programmers(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True)
    joined = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    programmer_name = models.ForeignKey('Programmers', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return f"{self.title} created by {self.programmer_name}"