from django.db import models


# Create your models here.
from answer.models import Answer
from question.models import Question
from user_profile.models import UserProfile


class Vote(models.Model):
    type = models.BooleanField(default=None)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')

    emitter_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, default='', blank=True, related_name='emitterProfile')
    receiver_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, default='', blank=True, related_name='receiverProfile')
    question_id = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, default='', blank=True, related_name='question')
    answer_id = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True, default='', blank=True, related_name='answer')

    def __str__(self):
        return self.type
