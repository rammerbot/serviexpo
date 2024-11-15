from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Experience, Education, Technology, Skill

# Create your views here.
def resume_view(request):
    educations = Education.objects.all().order_by('-date')

    context = {
        'educations': educations,
    }

    return render(request, 'resume/resume.html',context)

class TestView(TemplateView):

    template_name = 'test/test.html'