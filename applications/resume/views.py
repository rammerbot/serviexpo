from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Experience, Education, Technology, Skill

# Create your views here.
def resume_view(request):
    experiences = Experience.objects.all().order_by('-date')
    educations = Education.objects.all().order_by('-date')
    technologies = Technology.objects.all()
    skills = Skill.objects.all()

    context = {
        'experiences':experiences,
        'educations': educations,
        'technologies': technologies,
        'skills' : skills
    }

    return render(request, 'resume/resume.html',context)

class TestView(TemplateView):

    template_name = 'test/test.html'