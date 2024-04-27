from django import forms
from .models import WorkCategory, WorkSubcategory, ServiceProvider


class ServiceProviderForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ServiceProvider
        fields = ['name', 'email', 'mobile', 'city', 'work_category', 'work_subcategory', 'password', 'repassword']
        widgets = {
            'work_category': forms.Select(attrs={'id': 'work_category'}),
            'work_subcategory': forms.Select(attrs={'id': 'work_subcategory'}),
        }
