from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=255, blank=False, null=False, unique=True)
  
  def __str__(self):
    return self.name

class Tag(models.Model):
  name = models.CharField(max_length=255, blank=False, null=False, unique=True)
  
  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField(max_length=255, blank=False, null=False)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tags, blank=True)
  
  def __str__(self):
    return self.title