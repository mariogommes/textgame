from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Page

# Create your views here.

def index(request):
	page = get_object_or_404(Page, pk=3)
	context = {'page':page}
	return render(request, 'game/index.html', context)

def book(request, page_id):
	page = get_object_or_404(Page, pk=page_id)
	context = {'page':page, 'alerta': 'acessado, id: ' + page_id}
	return render(request, 'game/book.html', context)