from django.db import models

# Create your models here.


class Chat(models.Model):
    username1 = models.CharField(max_length=100)
    username2 = models.CharField(max_length=100)
    attach = models.FileField(upload_to='jsonFiles')

    def __str__(self):
        return self.username1