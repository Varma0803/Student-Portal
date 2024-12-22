from django import forms
from .models import TableBooking

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = TableBooking
        fields = '__all__'