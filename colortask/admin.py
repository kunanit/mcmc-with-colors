from django.contrib import admin
from django.http import HttpResponse
from colortask.models import *
import csv

# export participant data
def export_participants_csv(modeladmin, request, queryset):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=participants.csv'
	writer = csv.writer(response, csv.excel)
	writer.writerow(['participant_id','start_time','target_color','completed','proposal_sd'])
	for p in Participant.objects.all():
		writer.writerow([p.pk,p.start_time,p.target_color,p.completed,p.proposal_sd])
	return response
export_participants_csv.short_description = 'Export participants csv file'

# export question data
def export_questions_csv(modeladmin,request,queryset):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=questions.csv'
	writer = csv.writer(response, csv.excel)
	writer.writerow(['participant_id','question_number','timestamp',
					'color_left','color_right','selected_color'])
	for q in Question.objects.all():
		writer.writerow([q.participant,q.question_number,q.timestamp,
					q.color_left,q.color_right,q.selected_color])
	return response
export_participants_csv.short_description = 'Export participants csv file'

class ParticipantAdmin(admin.ModelAdmin):
	actions = [export_participants_csv]
	list_display = ['pk','start_time','target_color','completed']

class QuestionAdmin(admin.ModelAdmin):
	actions = [export_questions_csv]
	list_display = ['participant','question_number','timestamp','selected_color']




admin.site.register(Participant,ParticipantAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Color)
admin.site.register(Parameter)