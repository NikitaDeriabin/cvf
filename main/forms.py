from .models import Store
from django.forms import ModelForm, TextInput, Textarea


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ["name", "description"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            })
        }
