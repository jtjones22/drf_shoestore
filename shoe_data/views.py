from django.shortcuts import render

# Create your views here.


def index(request):
    html = 'index.html'
    context = {}
    return render(request, html, context)
