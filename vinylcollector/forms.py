from django.forms import ModelForm
from vinylcollector.models import Vinyl
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class UserRegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, public_key=settings.RECAPTCHA_PUBLIC_KEY,
                               private_key=settings.RECAPTCHA_PRIVATE_KEY, label='ReCAPTCHA')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email already registered')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({"placeholder": 'Username'})
            self.fields['email'].widget.attrs.update({"placeholder": 'Email'})
            self.fields['password1'].widget.attrs.update({"placeholder": 'Password'})
            self.fields['password2'].widget.attrs.update({"placeholder": 'Confirm Password'})
            self.fields[field].widget.attrs.update({"class": "form-control", "autocomplete": "off"})


class VinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = ["artist", "album", "genres", "notes", "formats", "qty", "image", "user_rating"]


class DiscogsVinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = '__all__'
