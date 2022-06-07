from django.db import models
from tag.models import Tag
from user_profile.models import UserProfile


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=75, help_text='Enter a title')
    content = models.TextField(max_length=5000, help_text='Enter your question')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    total_votes = models.IntegerField(default=0, help_text='Number of votes')
    resolution = models.BooleanField(default=False)

    profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='questions')
    tags = models.ManyToManyField(Tag, blank=True, related_name='questions')

    def __str__(self):
        return self.title
