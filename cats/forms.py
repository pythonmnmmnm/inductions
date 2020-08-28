#/home/mnmmnm/django_projects/mysite/cats/forms.py
from django.forms import ModelForm
from cats.models import Breed

# Create the form class.
class MakeForm(ModelForm):
    class Meta:
        model = Breed
        fields = '__all__'
