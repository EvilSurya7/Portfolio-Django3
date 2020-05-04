from django.db import models

# Create your models here.

class Blogs(models.Model):

    title = models.CharField(max_length=70)
    description = models.TextField()
    date =  models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
