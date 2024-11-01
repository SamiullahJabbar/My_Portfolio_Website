from django.db import models

# Create your models here.


class contectus(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    messages=models.TextField()

    def __str__(self):
        return self.name

