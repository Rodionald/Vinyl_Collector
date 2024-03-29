from django.db.models import TextField
from django.forms import ModelForm, EmailField, CharField
from vinylcollector.models import Vinyl
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.conf import settings
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class UserRegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    email = EmailField(required=True)
    recaptcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, public_key=settings.RECAPTCHA_PUBLIC_KEY,
                               private_key=settings.RECAPTCHA_PRIVATE_KEY, label=False)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Этот email уже используется другим пользователем')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({"placeholder": 'Username'})
            self.fields['email'].widget.attrs.update({"placeholder": 'Email'})
            self.fields['password1'].widget.attrs.update({"placeholder": 'Password'})
            self.fields['password2'].widget.attrs.update({"placeholder": 'Confirm Password'})
            self.fields[field].widget.attrs.update({"class": "form-control", "autocomplete": "off"})


class UserResetPasswordForm(PasswordResetForm):

    email = EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Пользователь с таким адресом email не зарегистрирован')


class VinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['artist'].widget.attrs.update({"placeholder": 'Artist'})
            self.fields['album'].widget.attrs.update({"placeholder": 'Album'})
            self.fields['genres'].widget.attrs.update({"placeholder": 'Genres'})
            self.fields['notes'].widget.attrs.update({"placeholder": 'Notes'})
            self.fields['formats'].widget.attrs.update({"placeholder": 'Formats'})
            self.fields['qty'].widget.attrs.update({"placeholder": 'Qty'})
            self.fields['manufacture_region'].widget.attrs.update({"placeholder": 'Manufacture region'})
            self.fields['label'].widget.attrs.update({"placeholder": 'Label'})
            self.fields['year'].widget.attrs.update({"placeholder": 'Year'})
            # self.fields['image'].widget.attrs.update({"placeholder": 'Image'})
            self.fields['user_rating'].widget.attrs.update({"placeholder": 'User rating'})
            self.fields[field].widget.attrs.update({"class": "form-control", "autocomplete": "off"})


class DiscogsVinylForm(ModelForm):
    class Meta:
        model = Vinyl
        fields = '__all__'
