from django.shortcuts import render

from .models import Home, InfoHome, Reasons
from applications.resume.models import Skill, Technology
from applications.contact.models import SocialMedia

# Create your views here.

def home_view(request):
    social_media = SocialMedia.objects.all().first()
    home = Home.objects.all().first()
    home_info = InfoHome.objects.all().first()
    skills = Skill.objects.all()
    technologies = Technology.objects.all()
    reasons = Reasons.objects.all().order_by('position')

    context = {
        'reasons' : reasons,
        'home_info': home_info,
        'skills' : skills,
        'technologies' : technologies,
        'company': home.company,
        'service_1': home.service_1,
        'service_2': home.service_2,
        'service_3': home.service_3,
        'slogan_short' : home.slogan,
        'slogan_large': home.slogan_1,
        'about':home.about,
        'image' : home.image,
        'facebook': social_media.facebook,
        'x': social_media.x,
        'instagram':social_media.instagram,
        'github': social_media.github,
        'linkedin': social_media.linkedin,


    }

    return render(request, 'home/index.html',context)