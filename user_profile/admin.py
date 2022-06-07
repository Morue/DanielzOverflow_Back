from django.contrib import admin
from user_profile.models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'status', 'total_points')
    list_filter = ('status', )
    list_per_page = 15
    # fields = []


admin.site.register(UserProfile, UserProfileAdmin)
