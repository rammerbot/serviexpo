from django.shortcuts import render
from .models import Project
# Create your views here.

def project_view(request):

    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project/project.html',context)