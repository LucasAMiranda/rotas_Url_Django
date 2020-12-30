from django.http import HttpResponse

# Create your views here.
def hello(request, nome, idade):
	return HttpResponse("<h1>Hello {} de {} anos</h1>".format(nome, idade));

def article(request, article_value):
	return HttpResponse('<h2>O nome article é {} '. format(article_value));