from django.db import models
from datetime import datetime, timedelta
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"
        
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        if len(USER.objects.filter(email=postData['email'])) > 0:
            errors["email"] = "Email should be unique"


        if len(postData['birthday']) == 0 :
            errors["birthday"] = "Birthday cannot be empty."
        elif datetime.strptime(postData['birthday'], "%Y-%m-%d") >=  datetime.today():
            errors["birthday"] = "Birthday needs to be in the past!"
        elif datetime.strptime(postData['birthday'], "%Y-%m-%d") < datetime.today() - timedelta(days=4745):
            errors["birthday"] = "Must be at least 13years old."

        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters."
        if postData['confrim_PW'] == postData['password']:
            errors["password"] = "Passwords need to match."

        return errors

class USER(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
