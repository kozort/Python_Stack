from django.db import models
    
class BOOK(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AUTHOR(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    description = models.TextField()
    Books = models.ManyToManyField(BOOK, related_name="Authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)