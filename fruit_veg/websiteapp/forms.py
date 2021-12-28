from django.forms import ModelForm
from .models import Emails

class EmailForm(ModelForm):
    class Meta:
        model = Emails
        fields = '__all__'