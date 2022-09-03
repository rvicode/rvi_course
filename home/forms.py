from django import forms

from blog.models import ContactUs, Course


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('subject', 'massage', )


class ContactUsUserForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'


class UpdateVideoForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'category', 'field', 'language', 'description', 'image', 'file', 'time_video', )
