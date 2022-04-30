from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from requests import request

from tweets.models import Tweet # or simpler from .models import Tweet (same directory)

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello world!!!</h1>")

def tweet_detail_view(request, pk):
    """
    REST API VIEW
    return json data
    Consume by JavaScript or Swift or Java or iOS/Android
    """
    data ={
        "pk": pk,
        # "image_path": obj.image.url
    } 
    status = 200
    
    try:
        obj = Tweet.objects.get(pk=pk)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
        

    
    return JsonResponse(data, status=status)

def dynamic_routing(request, name, *args, **kwargs):
    return HttpResponse(f"<h1> Hello {name}. Have a nice day")       

