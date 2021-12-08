from django import forms
from django.core.mail import EmailMessage, message
from django.conf import settings

class InquiryForm(forms.Form):
    name = forms.CharField(label='名前', max_length=50)
    email = forms.EmailField(label='メールアドレス')
    inquiry = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea(attrs={'rows':5, 'cols':16}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        inquiry = self.cleaned_data['inquiry']

        message = EmailMessage(subject=name + "さんからの問い合わせ",
                                body=inquiry,
                                from_email=email,
                                to=[settings.EMAIL_HOST_USER],
                                cc=[email])
        message.send()