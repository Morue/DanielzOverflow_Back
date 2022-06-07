from django.db import models


# Create your models here.
from user_profile.models import UserProfile


class Friendship(models.Model):
    status = models.CharField(max_length=50, default='sendFriendRequest')

    profile_one = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='profile_one')
    profile_two = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='profile_two')

    def __str__(self):
        return self.status
