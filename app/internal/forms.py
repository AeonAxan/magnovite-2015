from django import forms
import random

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    college = forms.CharField(max_length=50)
    mobile = forms.CharField(max_length=10)
    referral = forms.CharField(max_length=50, required=False)
    pack = forms.CharField(max_length=10)

    def clean(self):
        super(RegistrationForm, self).clean()
        email = self.cleaned_data.get('email', '')
        name = self.cleaned_data.get('name', '')
        college = self.cleaned_data.get('college', '')

        if not email:
            email = str(random.random()) + name[:8] + '|' + college[:5] + '@onspot.com'
            self.cleaned_data['email'] = email.replace(' ', '_')

        return self.cleaned_data

    def clean_mobile(self):
        mobile = str(self.cleaned_data['mobile'])

        # accept empty
        if mobile == '':
            return mobile

        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError('Mobile must be 10 digits')

        return mobile

    def clean_pack(self):
        pack = self.cleaned_data['pack']

        if pack not in ('single', 'multiple', 'none'):
            raise forms.ValidationError('Pack should be either single/multiple')

        return pack


