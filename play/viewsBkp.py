from django.shortcuts import render
from django.http import HttpResponse
from random import randrange as rand

# Create your views here.

class Play:
	def __init__(self):
		self.score=rand(6)

	def __str__(self):
		return str(self.score)

joueur=Play()

def post_list(request):
	return render(request, 'play.html')

print(joueur.score)
