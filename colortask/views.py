from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from scipy.stats import multivariate_normal, uniform, bernoulli, gaussian_kde
from datetime import datetime
from colortask.models import Participant,Question
# import numpy as np

### website views ###

def index(request):
	return render(request,'colortask/index.html')

def instructions(request):
	return render(request,'colortask/instructions.html')

def stage(request):
	p = Participant(start_time=datetime.now(),target_color='blue')
	context = {'userid':p.pk}
	return render(request,'colortask/stage.html',context)

def conclusion(request):
	return render(request,'colortask/conclusion.html')



### helper functions ###

# from http://code.activestate.com/recipes/266466-html-colors-tofrom-rgb-tuples/
def RGBToHTMLColor(rgb_tuple):
    """ convert an (R, G, B) tuple to #RRGGBB """
    hexcolor = '#%02x%02x%02x' % rgb_tuple
    # '%02x' means zero-padded, 2-digit hex values
    return hexcolor

# from http://code.activestate.com/recipes/266466-html-colors-tofrom-rgb-tuples/
def HTMLColorToRGB(colorstring):
	""" convert #RRGGBB to an (R, G, B) tuple """
	colorstring = colorstring.strip()
	if colorstring[0] == '#': colorstring = colorstring[1:]
	if len(colorstring) != 6:
		raise ValueError, "input #%s is not in #RRGGBB format" % colorstring
	r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
	r, g, b = [int(n, 16) for n in (r, g, b)]
	return (r, g, b)


### data-returning functions / MCMC modules ###
def initialize(request):
	x_t = (uniform().rvs(size=3)*256).astype(int).tolist()
	return HttpResponse(RGBToHTMLColor(tuple(x_t)))


def proposal(request):
	x_t = HTMLColorToRGB(request.GET['prevcolor'])

	# proposal distribution parameters
	mean_prop = x_t
	sd_prop = 30
	cov_prop = [[sd_prop**2,0,0],[0,sd_prop**2,0],[0,0,sd_prop**2]]

	# draw sample from proposal distribution, checking if out-of-bounds
	x_proposal = [-1]
	while any(xi<0 or xi>255 for xi in x_proposal):
		x_proposal = multivariate_normal(mean_prop,cov_prop).rvs().astype(int)
	return HttpResponse(RGBToHTMLColor(tuple(x_proposal)))


def save(request):

	return HttpResponse()

