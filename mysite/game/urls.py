from django.conf.urls import url
from . import views

app_name = 'game'

urlpatterns =[
	url(r'^$', views.index, name="index"),
	url(r'^(?P<page_id>\d+(?:\.\d+)*)/$', views.book, name="book"),
	
	# DESCOBRI O ERRO NO PATERN, NÂO ESTÀ ACEITANDO 1.x, antes eram só numeros, agora são strings
	# MUDAR O PATTERN
]