from django.contrib import admin
from friendship.models import Friendship


# Register your models here.
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('status', )
    list_filter = ('status', )


admin.site.register(Friendship, FriendshipAdmin)
