from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomEmail
from django import forms
class CustomUsercreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')

class CustomEmailForm(forms.ModelForm):
    class Meta:
        model = CustomEmail
        fields = ('to_email_address', 'title', 'content', 'img')
    def clean_to_email_address(self):
        to_email_address = self.cleaned_data['to_email_address']
        if not len(get_user_model().objects.filter(email=self.cleaned_data['to_email_address'])):
            raise ValidationError('이메일이 유효하지 않습니다.')
        return to_email_address