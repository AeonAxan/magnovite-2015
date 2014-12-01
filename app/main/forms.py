from django import forms
from django.forms import ModelForm

from .models import Profile


class ProfileForm(ModelForm):

    def clean_mobile(self):
        mobile = str(self.cleaned_data['mobile'])

        # accept empty
        if mobile == '':
            return mobile

        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError('Mobile must be 10 digits')

        return mobile

    def clean_year(self):
        year = self.cleaned_data['year']

        # accept blank
        if not year:
            return year

        if year not in [1, 2, 3, 4, 5]:
            raise forms.ValidationError('Must be a number between 1 and 5')

        return year

    class Meta:
        model = Profile
        fields = ['active_email', 'name', 'mobile', 'college', 'year']
