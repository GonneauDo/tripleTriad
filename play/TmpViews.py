from django.http import HttpResponse
from random import randrange as rand

def post_list(request):
	score=rand(6)
	html="<html><body><p style=color:red>Score : %s</p></body></html>" %score
	return HttpResponse(html)
