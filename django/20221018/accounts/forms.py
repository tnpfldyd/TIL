from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email):
            raise ValidationError('중복된 이메일이 있습니다.')
        return email