# tenders/forms.py
from django import forms
from main.models import Tender

class TenderForm(forms.ModelForm):
    class Meta:
        model = Tender
        fields = ['title', 'description', 'category', 'document', 'deadline']
