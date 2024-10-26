from django.shortcuts import render
from django.http import HttpResponse
#import datetime
# Create your views here.

def home(request):
    #html = "<html><body>Hello World</body></html>"

    context = {
        'greetings': 'ご挨拶',
        'introduction': 'Welcome to my project'
    }

    return render(request, 'home.html', context)