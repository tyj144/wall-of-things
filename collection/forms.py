from django.forms import ModelForm

from collection.models import Thing

# creates a form to edit a Thing object using Django's ModelForm
class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'description',)
