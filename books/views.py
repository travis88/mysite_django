from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

def search_form(request):
	return render(request, 'search_form.html')

def search(request):
	error = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error.append('Enter a search term.')
		elif len(q) > 20:
			error.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_results.html',
										{'books':books, 'query':q})
	return render(request, 'search_form.html', {'errors':error})
