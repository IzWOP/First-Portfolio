from django.shortcuts import render

def index(request):
    return render(request, 'blog/home.html',)
# Create your views here.
