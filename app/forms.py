from django import forms
from .models import testuser1
class studentregsitration(forms.ModelForm):
    class Meta:
        model = testuser1
        fields = ['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','id':'passwordid'})
        }