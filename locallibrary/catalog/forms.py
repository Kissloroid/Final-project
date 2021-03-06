from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        #Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом).
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        #Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Имя",
        widget=forms.TextInput
    )

    email = forms.EmailField(
        widget=forms.EmailInput
    )

    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea
    )


class UserForm(AuthenticationForm):
    class Meta:
        model = User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email',)
