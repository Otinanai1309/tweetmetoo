from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
# import pkg_resources
from requests import request


from .forms import TweetForm
from tweets.models import Tweet # or simpler from .models import Tweet (same directory)

import random

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.save()
        form = TweetForm() # reinitialize a new blank form
    return render(request, 'components/form.html', context={"form": form}, status=200)


def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    return json data
    Consume by JavaScript or Swift or Java or iOS/Android
    """
    qs = Tweet.objects.all()
    # My approach witch by the way i think is simpler    
    for tweet in qs:
        data = {
            'id': tweet.id,
            'content': tweet.content,
        }
    # Or another way to tacle this:
    tweets_list = []
    # with 1 or many lines 
    # tweet_list = [{"id": x.id, "content": x.content} for x in qs]
    for tweet in qs:
        tweets_list.append({
            'id': tweet.id,
            'content': tweet.content,
            'likes': random.randint(0, 1459)
        })
    data = {
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

