from django.db import models


class Participant(models.Model):
	start_time = models.DateTimeField()
	target_color = models.CharField(max_length=100)

class Question(models.Model):
	participant = models.ForeignKey(Participant)
	question_number = models.IntegerField()
	timestamp = models.DateTimeField()
	color1 = models.CharField(max_length=7)
	color2 = models.CharField(max_length=7)
	selected_color = models.CharField(max_length=7)

