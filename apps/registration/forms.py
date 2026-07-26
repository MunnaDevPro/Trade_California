from django import forms
from .models import RegistrationRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Row, Column, HTML

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationRequest
        fields = ["full_name", "company_name", "email", "phone", "country", "role", "message"]
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3, 'class': 'text-sm'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'e.g. John Doe',
            'company_name': 'e.g. ACME Corp',
            'email': 'e.g. john@example.com',
            'phone': 'e.g. +1 (555) 000-0000',
            'country': 'e.g. United States',
            'message': 'Briefly describe your requirements or inquiry...',
        }
        for field_name, field in self.fields.items():
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]
                
            if field_name != 'role':
                field.widget.attrs.update({
                    'class': 'bg-slate-50 border border-slate-300 text-slate-900 rounded-md focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 focus:bg-white transition-all duration-200 w-full px-3 py-2 text-sm outline-none'
                })
            
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # Modern, flat styling without shadows
        self.helper.layout = Layout(
            Row(
                Column('full_name', css_class='form-group col-span-1'),
                Column('company_name', css_class='form-group col-span-1'),
                css_class='grid grid-cols-1 md:grid-cols-2 gap-4 mb-3'
            ),
            Row(
                Column('email', css_class='form-group col-span-1'),
                Column('phone', css_class='form-group col-span-1'),
                css_class='grid grid-cols-1 md:grid-cols-2 gap-4 mb-3'
            ),
            Row(
                Column('country', css_class='form-group col-span-1'),
                Column('role', css_class='form-group col-span-1'),
                css_class='grid grid-cols-1 md:grid-cols-2 gap-4 mb-3'
            ),
            Column('message', css_class='mb-3'),
            HTML('<div class="mt-5 mb-2">'),
            Submit('submit', 'Submit Application', css_class='w-full bg-slate-900 text-white text-sm font-semibold py-2.5 px-4 rounded-md border-0 cursor-pointer hover:bg-slate-800 transition-colors'),
            HTML('</div>')
        )
