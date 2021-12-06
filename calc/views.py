from django.shortcuts import render

def index(request):
    return render(request, 'calc/index.html')

def description(request):
    return render(request, 'calc/description.html')
