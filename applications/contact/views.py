from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Contact, SocialMedia
from .forms import ContactForm


# Create your views here.

# Vista de contactos

def contact_view(request):

    social_media = SocialMedia.objects.all().first()
    form = ContactForm()
   # Datos para el front    
    context = {
        'facebook': social_media.facebook,
        'x': social_media.x,
        'instagram':social_media.instagram,
        'github': social_media.github,
        'linkedin': social_media.linkedin,
        'form': form
    }

    # Capturando el metodo post y creando el objeto contact
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message'],
                )
            contact.save()
            return redirect(reverse('contact:contact'))

    return render(request, 'contact/contact.html',context)