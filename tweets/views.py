from django.http import HttpResponse
from django.shortcuts import render
from requests import request

from tweets.models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello world!!!</h1>")

def tweet_detail_view(request, pk):
    obj = Tweet.objects.get(pk=pk)
    return HttpResponse(obj.content) 

def dynamic_routing(request, name, *args, **kwargs):
    return HttpResponse(f"<h1> Hello {name}. Have a nice day")       

