from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.safestring import mark_safe
from .models import Profile
from .attrs import attrs

class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f_name, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'
            f.widget.attrs['placeholder'] = attrs['placeholder'].get(f_name, '')
            f.label = attrs['label'].get(f_name, f_name.capitalize())
            f.label_suffix = ''
            f.help_text = attrs['help_text'].get(f_name, '')
            f.error_messages = attrs['error_messages'].get(f_name, {})

    def as_div(self):
        o = []
        for f in self:
            code = f'<div class="form-group mb-3">{f.label_tag()}{f}</div>'
            o.append(code)
        return mark_safe('\n'.join(o))

class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'username', 'profile_picture', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f_name, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'
            f.widget.attrs['placeholder'] = attrs['placeholder'].get(f_name, '')
            f.label = attrs['label'].get(f_name, f_name.capitalize())
            f.label_suffix = ''
            f.help_text = attrs['help_text'].get(f_name, '')
            f.error_messages = attrs['error_messages'].get(f_name, {})

    def as_div(self):
        o = []
        for f in self:
            if f.name == 'password':
                continue
            code = f'<div class="form-group mb-3">{f.label_tag()}{f}</div>'
            o.append(code)
        return mark_safe('\n'.join(o))