from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """ Define input type for calendar picker """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """ The Booking Form Model """
    class Meta:
        """ Fields list and widget """
        model = Booking

        fields = ['car', 'name', 'email', 'phone', 'date', 'message']
        widgets = {
            'car': forms.TextInput(attrs={'class': 'form-control',
                                          'readonly': 'readonly'}),
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'readonly': 'readonly'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control',
                                           'type': 'date'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
