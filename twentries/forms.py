from django import forms
from twentries.models import Twentry

class TwentryForm(forms.ModelForm):
    content = forms.CharField(max_length=140, widget=forms.Textarea)
    
    class Meta:
        model = Twentry
        fields = ('content',)