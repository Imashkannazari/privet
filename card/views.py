from django.shortcuts import render
from . models import Projects, Programmers
from django.shortcuts import get_object_or_404
def card(request):
    project = Projects.objects.all()
    return render(request, 'projects list.html', {"project":project})

def detail(request, slug):
    projects=get_object_or_404(Projects, slug=slug)
    return render(request, 'detail.html',   {'projects':projects})

def programmers(request):
    programmer = Programmers.objects.all()
    return render(request, 'programmers list.html', {"programmer":programmer})
def home(request):
    return render(request, 'index.html')