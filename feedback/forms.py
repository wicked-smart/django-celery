from django import forms
from django.core.mail import send_mail
from time import sleep


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="email", widget=forms.EmailInput(
        attrs={"style": "margin-bottom: 10px;" }
    ))
    subject = forms.CharField(label="subject", max_length=100, widget=forms.TextInput(
        attrs = {'style': 'margin-bottom: 10px;'}
    ))
    feedback = forms.CharField(label="feedback", widget=forms.Textarea(
        attrs={"rows": 5, "style": "margin-top: 10px;"}
        ))
    


        


