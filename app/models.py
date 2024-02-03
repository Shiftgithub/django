from django.db import models

class Session(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "session"