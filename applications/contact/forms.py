from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('__all__')

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id':'name',
                    'placeholder':'ingresa tu nombre..',
                    'data-sb-validations':'required'
                    }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'id':'email',
                    'placeholder':'name@example.com...',
                    'data-sb-validations':'required'
                    }
            ),
              'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id':'phone',
                    'placeholder':'(123)...',
                    'data-sb-validations':'required'
                    }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id':'message',
                    'placeholder':'Ingrese su mensaje aqui',
                    'data-sb-validations':'required',
                    'style':'height: 10rem'
                    }
            )

        }