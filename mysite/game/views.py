from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Page

# Create your views here.

def index(request):
	context = {}
	return render(request, 'game/index.html', context)

def book(request, page_id=1):
	print("PAGE ID: ", page_id)
	page = get_object_or_404(Page, pk=page_id)
	mock_id= '2'
	context = {'page':page , 'id':mock_id}
	return render(request, 'game/book.html', context)