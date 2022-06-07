from django.db import models

# Create your models here.


class Tag(models.Model):
    label = models.CharField(max_length=50, help_text='Enter a tag name')

    def __str__(self):
        return self.label
