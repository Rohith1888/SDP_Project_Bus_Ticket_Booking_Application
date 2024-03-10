# forms.py

# forms.py

from django import forms

class BusSearchForm(forms.Form):
    from_location = forms.CharField(label='From', max_length=100)
    to_location = forms.CharField(label='To', max_length=100)
    date = forms.DateField(label='Date')

