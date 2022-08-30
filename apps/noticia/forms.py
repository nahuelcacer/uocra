from django import forms
from .models import Categoria

class AgregarCategoria(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows':'2', 
            'placeholder':'Nueva categoria...',
            'class':'form-control'
            }), required=True, max_length=250, label='')
    class Meta:
        model = Categoria
        fields = ['nombre']