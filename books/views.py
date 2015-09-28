# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book
def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	#error = False
	errors=[]
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			#error = True
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			#message = 'You searched for: %r' % request.GET['q']
			return render_to_response('search_results.html', {'books':books, 'query':q})
		#message = 'You submitted an empty form'
		#return HttpResponse('Please submit a search term.')
	return render_to_response('search_form.html', {'errors':errors})
	#return HttpResponse(message)

