from django.db import models
from datetime import datetime


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(SHOW.objects.filter(title=postData['title'])) > 0:
            errors["title"] = "Title should be unique"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if 0 < len(postData['description']) < 10:
            errors["description"] = "Description is optional but should be at least 10 characters"
        if len(postData['release_date']) == 0 :
            errors["release_date"] = "Release date is empty."
        elif datetime.strptime(postData['release_date'], "%Y-%m-%d") >=  datetime.today():
            errors["release_date"] = f"Release date needs to be in the past"
        elif datetime.strptime(postData['release_date'], "%Y-%m-%d") < datetime.strptime("1900-01-01", "%Y-%m-%d"):
            errors["release_date"] = f"Release date too old!"
        
        #check if title is unique
        


        return errors


class SHOW(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    # Stranger Things