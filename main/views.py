from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import Url
from django.contrib.messages import add_message, SUCCESS, get_messages


def home(request):
    messages = list(get_messages(request))
    return render(request, 'home.html', {'shortened_url': messages[0] if messages else None})

def shorten_url(request):
    url = request.POST['url']
    url_obj = Url.objects.create(url=url, owner=request.user if request.user.is_authenticated else None)
    shortened_url = request.build_absolute_uri('/' + url_obj.key)
    message = f'Your shortened url is: \n\n{shortened_url}'
    add_message(request, SUCCESS, message)
    return redirect('home')

def open_url(request, key):
    url =  get_object_or_404(Url, key=key)
    url.clicks += 1
    url.save()
    return redirect(url.url)
