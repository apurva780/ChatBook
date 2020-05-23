from django.db import models

# Create your models here.


class Chat(models.Model):
    username1 = models.CharField(max_length=15)
    username2 = models.CharField(max_length=15)
    attach = models.FileField()

    def __str__(self):
        return self.username1