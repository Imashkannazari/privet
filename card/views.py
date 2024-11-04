from django.shortcuts import render
from . models import Projects
def card(request):
    project = Projects.objects.all()
    return render(request, 'projects list.html', {"project":project})

def detail(request, id):
    projects = Projects.objects.get(id=id)
    return render(request, 'detail.html', {"projects":projects})