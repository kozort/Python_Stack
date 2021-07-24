from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        return errors

class TripManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        return errors

class USER(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#   trips_created = a list of trips the user created
#   trips_joined = a list of trips the user is going on

    objects = UserManager()

class TRIP(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    Plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(USER, related_name="trips_created", on_delete=models.CASCADE) # a user who created this trip
    travelers = models.ManyToManyField(USER, related_name="trips_joined") # a list of users that joined this trip

    objects = TripManager()
