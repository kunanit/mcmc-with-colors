from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from numpy import diag
from numpy.random import multivariate_normal, uniform
from datetime import datetime
from colortask.models import Participant,Question,Parameter,Color
import random


### website views ###

def index(request):
	return render(request,'colortask/index.html')

def instructions_mturk(request):
	context = {'mturk':True}
	return render(request,'colortask/instructions.html',context)	

def instructions(request):
	return render(request,'colortask/instructions.html')

def stage(request):
	if 'mturk' in request.GET:
		from_mturk = True
	else: from_mturk = False

	# choose the target color
	colorchoices = [c.color for c in Color.objects.all()]
	target_color = random.choice(colorchoices)

	# mcmc parameters
	params = Parameter.objects.all().first()

	p = Participant(start_time=datetime.now(),
					target_color=target_color,
					proposal_sd=params.proposal_sd,
					from_mturk=from_mturk)
	p.save()

	# compute an initial color, sampled uniformly
	x_t = uniform(high=256,size=3).astype(int)
	# initial_color = RGBToHTMLColor(tuple(x_t.tolist()))

	initial_color = "rgb({0},{1},{2})".format(x_t[0],x_t[1],x_t[2])

	context = {'userid':p.pk,
			'initialColor':initial_color,
			'targetColor':target_color,
			'proposalSD':params.proposal_sd,
			'maxQuestions':params.max_questions,
			'mturk':from_mturk}
	return render(request,'colortask/stage.html',context)

def conclusion(request):

	# record that participant finished question set
	userid = request.GET['userid']
	p = Participant.objects.get(pk=userid)
	p.completed = True

	if p.from_mturk:
		if not p.mturk_code:
			# generate "random" code
			letters = ''.join([chr(random.randint(97,122)) for i in range(4)])
			p.mturk_code = "{0}{1}".format(letters,userid)
			p.save()

		context = {'code':p.mturk_code}

		return render(request,'colortask/conclusion_mturk.html',context)

	p.save()
	return render(request,'colortask/conclusion.html')



### helper functions ###

# from http://code.activestate.com/recipes/266466-html-colors-tofrom-rgb-tuples/
def RGBToHTMLColor(rgb_tuple):
    """ convert an (R, G, B) tuple to #RRGGBB """
    hexcolor = '#%02x%02x%02x' % rgb_tuple
    # '%02x' means zero-padded, 2-digit hex values
    return hexcolor

# from http://code.activestate.com/recipes/266466-html-colors-tofrom-rgb-tuples/
# def HTMLColorToRGB(colorstring):
# 	""" convert #RRGGBB to an (R, G, B) tuple """
# 	colorstring = colorstring.strip()
# 	if colorstring[0] == '#': colorstring = colorstring[1:]
# 	if len(colorstring) != 6:
# 		raise ValueError, "input #%s is not in #RRGGBB format" % colorstring
# 	r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
# 	r, g, b = [int(n, 16) for n in (r, g, b)]
# 	return (r, g, b)


### data-returning functions / MCMC modules ###

def proposal(request):
	# prevcolor has format 'rgb(123,45,67)'
	x_t = tuple([int(i) for i in request.GET['prevcolor'].strip('rgb()').split(',')])
	# x_t = HTMLColorToRGB(request.GET['prevcolor'])
	sd_prop = float(request.GET['proposalSD'])

	# proposal distribution parameters
	mean_prop = x_t
	# sd_prop = 50
	cov_prop = diag([sd_prop**2]*3)

	# draw sample from proposal distribution, checking if out-of-bounds
	x_proposal = [-1]
	while any(xi<0 or xi>255 for xi in x_proposal):
		x_proposal = multivariate_normal(mean_prop,cov_prop).astype(int)

	# return has html color code, e.g. #f0f0f0
	return HttpResponse(RGBToHTMLColor(tuple(x_proposal)))

def saveQuestionData(request):
	# create new object to store in database
	userid = request.GET['userid']
	p = Participant.objects.get(pk=userid)
	q = Question(
			participant=p,
			question_number=request.GET['currentQuestion'],
			color_left=request.GET['color0'],
			color_right=request.GET['color1'],
			selected_color=request.GET['selectedColor'],
			timestamp=datetime.now(),
			)
	q.save()

	return HttpResponse()

# def saveParticipantData(request):
# 	# record that participant finished question set
# 	userid = request.GET['userid']
# 	p = Participant.objects.get(pk=userid)
# 	p.completed = True
# 	p.save()

# 	return HttpResponse()
