from django.contrib import admin
from answer.models import Answer


# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('summary', 'total_votes', 'created_at')


admin.site.register(Answer, AnswerAdmin)
