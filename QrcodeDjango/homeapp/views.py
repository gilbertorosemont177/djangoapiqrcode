from django.shortcuts import render

# Create your views here.
def index(request):
	numbers=["susana","gilberto","eduardo"]
	prenom = 'susana'
	args = {'nom' : prenom, 'liste':numbers}
	
	return render(request,'homeapp/index.html', args)
