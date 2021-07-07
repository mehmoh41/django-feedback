from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # files are not stored in database it is a bad practice
    # instead files should be stored in hard stores
    # and only stores the path in the database

    image = models.ImageField(upload_to="images")
