from .models import item_model
from django.forms import ModelForm

class item_form(ModelForm):
    class Meta:
        model = item_model
        fields = '__all__'