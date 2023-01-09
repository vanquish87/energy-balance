from django.forms import ModelForm
from django import forms
from .models import Weight

class WeightForm(ModelForm):
    class Meta:
        model = Weight
        # django will create all the fiels according to model with __all__
        # fields = '__all__'
        fields = ['weight', 'calorie_intake', 'date']
        # with this we are modifying classes in html for form
        widgets = {
            'date': forms.DateField()
            }

    def __init__(self, *args, **kwargs):
        super(WeightForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'add title'})

        # self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'add descriptioon'})
