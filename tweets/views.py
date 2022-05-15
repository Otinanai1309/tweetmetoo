import json
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils.http import is_safe_url
from requests import request
# from rest_framework import serializers
from .serializers import TweetSerializer

from tweetmetoo.settings import ALLOWED_HOSTS


from .forms import TweetForm
from tweets.models import Tweet # or simpler from .models import Tweet (same directory)

import random

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data = request.POST or None)
    if serializer.is_valid():
        serializer.save(user = request.user)
        return JsonResponse(serializer.data, status = 201)
    return JsonResponse({}, status=400)

def tweet_create_view_pure_django(request, *args, **kwargs):
    # print("ajax:", request.headers.get('x-requested-with') == 'XMLHttpRequest')
    user = request.user 
    if not request.user.is_authenticated:
        user = None
        if request.is_ajax():
            return JsonResponse({}, status=401)  # as in Not authorized
        return redirect(settings.LOGIN_URL)
    
    form = TweetForm(request.POST or None)
    print('post data is:', request.POST)
    next_url = request.POST.get("next") or None
    print('next_url:', next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.user = user
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)  # 201 is typically for created items
        
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        
        form = TweetForm() # reinitialize a new blank form
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'components/form.html', context={"form": form}, status=200)


def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    return json data
    Consume by JavaScript or Swift or Java or iOS/Android
    """
    qs = Tweet.objects.all()
     
    tweets_list = [x.serialize() for x in qs]
    
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data, status=200)

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

