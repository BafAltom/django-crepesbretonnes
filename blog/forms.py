#-*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(label=u"Your email")
    sendCopy = forms.BooleanField(help_text=u"Do you want a copy of your mail sent to you?", require=False)

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')
        if subject and message:
            if "pizza" in subject and "pizza" in message:
                msg = u"Pizzas? In MY contact form?"
                self._errors["message"] = self.error_class([msg])
                del cleaned_data["message"]
        return cleaned_data
