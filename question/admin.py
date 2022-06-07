from django.contrib import admin
from question.models import Question


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'total_votes', 'resolution', 'created_at')
    list_filter = ('created_at', 'resolution')


admin.site.register(Question, QuestionAdmin)
