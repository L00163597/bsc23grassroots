from django import forms
from .models import User, Application, Grant, SpecialAward


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'address', 'password']

    def save(self, commit=True):
        # Ensure that the email provided is unique in the system
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('A user with that email already exists.')
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

