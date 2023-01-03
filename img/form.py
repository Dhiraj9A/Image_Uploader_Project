from django import forms
from .models import img_uploder

class img_form(forms.ModelForm):
    class Meta:
        model=img_uploder
        fields='__all__'
       
