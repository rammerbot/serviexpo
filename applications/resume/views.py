from django.shortcuts import render

from .models import Experience, Education, Technology, Skill

# Create your views here.
def resume_view(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    technologies = Technology.objects.all()
    skills = Skill.objects.all()

    context = {
        'experiences':experiences,
        'educations': educations,
        'technologies': technologies,
        'skills' : skills
    }

    return render(request, 'resume/resume.html',context)