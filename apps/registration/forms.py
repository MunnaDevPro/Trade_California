from django import forms
from .models import RegistrationRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Row, Column, HTML

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationRequest
        fields = ["full_name", "company_name", "email", "phone", "country", "role", "message"]
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # Modern, flat styling without shadows
        self.helper.layout = Layout(
            Row(
                Column('full_name', css_class='form-group col-span-1'),
                Column('company_name', css_class='form-group col-span-1'),
                css_class='grid grid-cols-1 md:grid-cols-2 gap-8 mb-4'
            ),
            Row(
                Column('email', css_class='form-group col-span-1'),
                Column('phone', css_class='form-group col-span-1'),
                css_class='grid grid-cols-1 md:grid-cols-2 gap-8 mb-4'
            ),
            Row(
                Column('country', css_class='form-group col-span-1'),
                Column('role', css_class='form-group col-span-1'),
                css_class='grid grid-cols-1 md:grid-cols-2 gap-8 mb-4'
            ),
            Column('message', css_class='mb-4'),
            HTML('<div class="mt-8 mb-4">'),
            Submit('submit', 'Submit Application', css_class='w-full bg-slate-900 text-white font-medium py-3 px-6 rounded-md border-0 cursor-pointer'),
            HTML('</div>')
        )
