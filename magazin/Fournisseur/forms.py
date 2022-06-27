from django.forms import ModelForm
<<<<<<< HEAD
=======
<<<<<<< HEAD
from django import forms
=======
>>>>>>> 8be79b34c5469a9341f0101d2a141bbadde9eb1b
>>>>>>> tempbranch
from .models import Fourn
class FournForm(ModelForm):
    class Meta:
        model =Fourn
<<<<<<< HEAD
        fields ='__all__'
=======
<<<<<<< HEAD
        fields ='__all__'
        widgets = {
            'Nom': forms.TextInput(attrs={'placeholder': 'Nom'}),
            'Tel':forms.TextInput(attrs={'placeholder':'Telephone'}),
            'Adresse':forms.TextInput(attrs={'placeholder':'adresse'}),
            'Cin':forms.TextInput(attrs={'placeholder':'Cin'}),
            'Email':forms.TextInput(attrs={'placeholder':'Email'})
        }
=======
        fields ='__all__'
>>>>>>> 8be79b34c5469a9341f0101d2a141bbadde9eb1b
>>>>>>> tempbranch
