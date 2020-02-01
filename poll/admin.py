from django.contrib import admin
from .models import Question,Choice

class ChoiceAdmin(admin.ModelAdmin):
	list_display=("question","choice_text","votes")

admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Question)