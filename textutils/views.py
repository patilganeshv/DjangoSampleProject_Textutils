from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return HttpResponse('''<h1>Jay Ganesh</h1> <a href ="https://www.google.com/search?q=jay+ganesh+jay+ganesh+deva&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjAhvTqqu3iAhVXWysKHcAeBVoQ_AUIEigD&biw=1360&bih=657">
						Django Demo</a>''')

def index1(request):
	param = { 'name': 'Ganesh' , 
			  'address': 'Pune',
			  'mo_no': '9021214411'
			}
	return render(request,'index.html',param)


def Navigation(request):

	s = '''<h1>Navigation Bar</h1>
		<a href = "https://www.google.com/">Google</a><br>
		<a href = "https://www.amazon.com/">Amazon</a><br>
		<a href = "https://www.flipkart.com/">Flipkart</a><br>
		<a href = "https://www.facebook.com/">Facebook</a><br>
		<a href = "https://www.olx.com/">olx</a>'''
	return HttpResponse(s)

def analyze(request):
	# Get The Text. 
	djtext = request.GET.get('text','default')

	#Check Checkbox Values
	removepunc = request.GET.get('removepunc','off')
	fullcaps = request.GET.get('fullcaps','off')
	newlineremover = request.GET.get('newlineremover','off')
	extraspaceremover = request.GET.get('extraspaceremover','off')

	# Check hich checkbox is on
	if removepunc == "on":
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		analyzed = " "
		for char  in djtext:
			if char not in punctuations:
				analyzed = analyzed + char 

		# Analyze the Text.
		param = {'purpose': 'Removed Punctuations', 'analyzed_text':analyzed }
		return render(request, 'analyze.html' ,param)
	
	# For Capitalize
	elif(fullcaps == "on"):
		analyzed = "" 
		for char in djtext:
			analyzed = analyzed + char.upper()
		param = {'purpose': 'Changed to UpperCase','analyzed_text':analyzed}
		return render(request,'analyze.html',param)

	#For Ne line Remover
	elif(newlineremover == "on"):
		analyzed = ""
		for char in djtext:
			if char != "\n":
				analyzed = analyzed + char

		param = {'purpose': 'New Line Remover','analyzed_text':analyzed}
		return render(request,'analyze.html',param)

	
	#Extra Space Remover
	elif(extraspaceremover == "on"):
		analyzed = ""
		for index,char in enumerate(djtext):
			print("index: ",index,"char: ",char)
			if djtext[index] == " " and djtext[index+1] == " ":
				pass
			else:	
				analyzed = analyzed + char

		param = {'purpose': 'Extra Space Remover','analyzed_text':analyzed}
		return render(request,'analyze.html',param)


	else:
		return HttpResponse("Error")


def ex1(request):
	pass