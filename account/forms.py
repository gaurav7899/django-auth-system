from django import forms
from account.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["email","name","password","confirm_password"]
    # vaidate password
    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password')
        confirm_password = clean_data.get('confirm_password')

        if password != confirm_password:
            self.add_error("password and confirm password doesn't match")
        return clean_data
    

    # check exiting email login or not

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already logged In/exists")
        return email
    