from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .attrs import attrs
from django.utils.safestring import mark_safe

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f_name, f in self.fields.items():
            css_class = 'form-check-input' if f_name == 'is_private' else 'form-control'
            f.widget.attrs['class'] = css_class
            f.widget.attrs['placeholder'] = attrs['placeholder'].get(f_name, '')
            f.label = attrs['label'].get(f_name, f_name.capitalize())
            f.label_suffix = ''
            f.help_text = attrs['help_text'].get(f_name, '')

    def as_div(self):
        output = []
        for f in self:
            if f.name == 'is_private':
                code = f'<div class="form-check mb-3">{f}{f.label_tag()}</div>'
            else:
                code = f'<div class="mb-3">{f.label_tag()}{f}</div>'
            output.append(code)
        return mark_safe('\n'.join(output))

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            'email', 'first_name', 'last_name', 'is_private', 'profile_picture', 'location',
            'company', 'website_url', 'instagram_username', 'telegram_username', 'facebook_username'
        ]
        exclude = ['password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f_name, f in self.fields.items():
            css_class = 'form-check-input' if f_name == 'is_private' else 'form-control'
            f.widget.attrs['class'] = css_class
            f.widget.attrs['placeholder'] = attrs['placeholder'].get(f_name, '')
            f.label = attrs['label'].get(f_name, f_name.capitalize())
            f.label_suffix = ''
            f.help_text = attrs['help_text'].get(f_name, '')

    def as_div(self):
        output = []
        for f in self:
            if f.name == 'password':
                continue
            if f.name == 'is_private':
                code = f'<div class="form-check mb-3">{f}{f.label_tag()}</div>'
            else:
                code = f'<div class="mb-3">{f.label_tag()}{f}</div>'
            output.append(code)
        return mark_safe('\n'.join(output))
