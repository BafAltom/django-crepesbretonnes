#-*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(label=u"Your email")
    sendCopy = forms.BooleanField(help_text=u"Do you want a copy of your mail sent to you?")

