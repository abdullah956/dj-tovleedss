from django import forms
from .models import Certificate

class CertificateForm(forms.ModelForm):
    issue_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}), 
        input_formats=["%Y-%m-%d"]
    )
    expiry_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}), 
        input_formats=["%Y-%m-%d"]
    )

    class Meta:
        model = Certificate
        fields = '__all__'
        widgets = {
            "card_no": forms.TextInput(attrs={"class": "form-control"}),
            "certificate_no": forms.TextInput(attrs={"class": "form-control"}),
            "operator_name": forms.TextInput(attrs={"class": "form-control"}),
            "company": forms.TextInput(attrs={"class": "form-control"}),
            "operator_trade": forms.TextInput(attrs={"class": "form-control"}),
            "iqama_number": forms.TextInput(attrs={"class": "form-control"}),
            "profile": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "undercard": forms.TextInput(attrs={"class": "form-control"}),
            
        }
