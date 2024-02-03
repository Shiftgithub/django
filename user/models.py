import os
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


def image_filepath(instance, filename):
    # Get the original filename
    old_filename = filename

    # Get the current timestamp
    time_now = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")

    # Generate a new filename using the timestamp and original filename
    filename = "%s_%s" % (time_now, old_filename)

    # Return the relative path to the folder where you want to save the image
    return os.path.join("uploads", "images", filename)


class User(AbstractUser):
    profile_pic = models.ImageField(upload_to=image_filepath, null=True)
    role = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = "user"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.is_staff = True
            if self.role == "admin":
                self.is_superuser = True
            elif self.is_superuser == True:
                self.role = "admin"
            else:
                self.is_superuser = False
            if self.password:
                self.password = make_password(self.password)
        super().save(*args, **kwargs)