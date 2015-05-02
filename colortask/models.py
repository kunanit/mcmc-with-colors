from django.db import models


class Participant(models.Model):
	start_time = models.DateTimeField()
	target_color = models.CharField(max_length=100)
	completed = models.BooleanField(default=False)
	proposal_sd = models.FloatField()
	def __unicode__(self):
		return "Participant {0}".format(self.pk)


class Question(models.Model):
	participant = models.ForeignKey(Participant)
	question_number = models.IntegerField()
	timestamp = models.DateTimeField()
	color_left= models.CharField(max_length=100)
	color_right = models.CharField(max_length=100)
	selected_color = models.CharField(max_length=100)

class Parameter(models.Model):
	proposal_sd = models.IntegerField()
	max_questions = models.IntegerField()
	def __unicode__(self):
		return "Default parameters"

class Color(models.Model):
	color = models.CharField(max_length=50)
	def __unicode__(self):
		return self.color