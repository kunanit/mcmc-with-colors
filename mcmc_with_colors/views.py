from django.shortcuts import render, redirect


def home(request):

	return redirect('/colortask/instructions')
	# return render(request,'colortask/home.html')