# Generated by Django 3.1.2 on 2021-03-26 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(help_text='Enter your firstname', max_length=50)),
                ('lastname', models.CharField(help_text='Enter your lastname', max_length=50)),
                ('pseudo', models.CharField(blank=True, default='Daniel-<django.db.models.fields.CharField>', help_text='Enter your pseudo, Daniel', max_length=30, unique=True)),
                ('biography', models.TextField(blank=True, default='', help_text='Enter your brilliant biography', max_length=160)),
                ('avatar', models.ImageField(default='/media/images/error-pic.png', help_text='Choose a picture', upload_to='media/images/')),
                ('total_points', models.IntegerField(default=10)),
                ('status', models.CharField(default='online', max_length=20)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
