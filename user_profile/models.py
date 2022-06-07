from django.contrib.auth import get_user_model
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)
    firstname = models.CharField(max_length=50, help_text='Enter your firstname', null=True, blank=True)
    lastname = models.CharField(max_length=50, help_text='Enter your lastname', null=True, blank=True)
    # TODO = auto-increment default pseudo
    pseudo = models.CharField(max_length=30, help_text='Enter your pseudo, Daniel', blank=True, null=True)
    biography = models.TextField(max_length=160, help_text='Enter your brilliant biography', blank=True, null=True)
    avatar_profile = models.ImageField(upload_to='images/', null=True, blank=True)
    total_points = models.IntegerField(default=10)
    # TODO = Status entity
    status = models.CharField(max_length=20, default="online")

    @property
    def avatar_profile_url(self):
        if self.avatar_profile and hasattr(self.avatar_profile, 'url'):
            return self.avatar_profile.url
        return ''

    def __str__(self):
        return self.pseudo


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, pseudo=instance.username)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

