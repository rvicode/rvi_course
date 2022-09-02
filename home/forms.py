from django import forms

from blog.models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('subject', 'massage', )


class ContactUsUserForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
