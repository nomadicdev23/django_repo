from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .forms import EmailForm

#dummy data for sake of 'working with data for now'
posts = [
    {
        'author': 'Samual',
        'birthday': 'August 05, 1901',
        'content': 'dskjgnlkndslknalsd,.as',
        'date_posted': 'June 20, 2020'
        
    },
    {
        'author': 'Connor',
        'birthday': 'August 05, 1954',
        'content': 'dskjgnlkndslknalsd,.as',
        'date_posted': 'June 29, 2020'
        
    },
    {
        'author': 'Connor',
        'birthday': 'August 05, 1954',
        'content': 'dskjgnlkndslknalsd,.as',
        'date_posted': 'June 29, 2020'
        
    }
]


def home(request):

    form = EmailForm()
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
         'form':form
    }
    response = requests.get('https://thatcopy.pw/catapi/rest/')
    catdata = response.json()
    contents = {
        "id" : catdata["id"],
        "url" : catdata["url"]
    }
    
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})




