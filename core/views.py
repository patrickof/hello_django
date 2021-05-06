from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request,nome,anos):
    return HttpResponse('<h1>Hello {} de {} </h1>'.format(nome,anos))