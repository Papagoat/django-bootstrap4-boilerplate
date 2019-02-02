from django.db import models

# Create your models here.
class Demo(models.Model):
    demo_title = models.CharField(max_length=200)
    demo_description = models.CharField(max_length=200)

    def __str__(self):
        return self.demo_title
