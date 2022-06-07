from django.db import models
from question.models import Question
from user_profile.models import UserProfile


# Create your models here.
class Answer(models.Model):
    summary = models.CharField(max_length=60, help_text='Resume of the content', default='')
    content = models.TextField(max_length=5000, help_text='Enter your answer', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    total_votes = models.IntegerField(default=0)

    profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True, related_name='answers')

    def __str__(self):
        return self.summary


