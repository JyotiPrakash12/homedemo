from django.db import models

# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length= 400)
    completed = models.BooleanField(default=False)
    cretaedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


