from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Page

# Create your views here.

def index(request):
	page = get_object_or_404(Page, pk="1")
	context = {'page':page, 'img_code': 'game/img/img1.png'}
	return render(request, 'game/index.html', context)

def book(request, page_id):
	page = get_object_or_404(Page, pk=page_id)
	context = {'page':page, 'img_code': 'game/img/img' + page_id + '.png'}
	return render(request, 'game/book.html', context)