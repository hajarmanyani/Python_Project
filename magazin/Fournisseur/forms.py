from django.forms import ModelForm
from .models import Fourn
class FournForm(ModelForm):
    class Meta:
        model =Fourn
        fields ='__all__'