from django.shortcuts import render

from .models import AboutPage

# Create your views here.


def about_view(request):

    about = AboutPage.objects.all().first()

   # Datos para el front    
    context = {
        'about': about,
        
    }

    return render(request, 'about/about.html',context)