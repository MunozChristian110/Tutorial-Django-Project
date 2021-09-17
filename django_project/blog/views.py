from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'Christian Munoz',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Cesar Munoz',
        'title': 'Blog Post 12',
        'content': 'more post content',
        'date_posted': 'August 29, 2018'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {'title':'About'})
