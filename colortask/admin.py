from django.contrib import admin
from colortask.models import *


class ParticipantAdmin(admin.ModelAdmin):
	list_display = ['pk','start_time','target_color','completed']

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['participant','question_number','timestamp','selected_color']

admin.site.register(Participant,ParticipantAdmin)
admin.site.register(Question,QuestionAdmin)