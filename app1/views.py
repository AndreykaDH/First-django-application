from django.shortcuts import render
from app1.models import Worker

def index_page(request):

	#allWorkers = Worker.objects.all()
	#dude = Worker.objects.
	#txt = {'name': 'none', 'second_name': 'none', 'salary': 'none'}
	#print(txt[name])
	#if dude==None: 
		#txt = {'name': 'none', 'second_name': 'none', 'salary': 'none'}
	#else:
		#print(dude)
		#txt = dude { dude.name, dude.second_name, salary } # = { 'putin': 'huilo ebanoe'}
	return render(request, 'index.html')
