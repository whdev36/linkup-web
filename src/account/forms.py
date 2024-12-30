# forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account
from django.utils.safestring import mark_safe

class AccountForm(UserCreationForm):
	class Meta:
		model = Account
		fields = ['email', 'first_name', 'last_name', 'username',  'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'
			field.widget.attrs['placeholder'] = ''
			# field.label = ''
			field.label_suffix = ''
			field.help_text = ''
			field.error_messages = {}

	def as_div(self):
		output = []
		for field in self:
			output.append(f'<div class="form-group mb-3">{field.label_tag()}{field}</div>')
		return mark_safe('\n'.join(output))

class AccountChangeForm(UserChangeForm):
	class Meta:
		model = Account
		fields = ['email', 'first_name', 'last_name', 'username',
			'picture', 'color', 'is_private', 'bio']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for field_name, field in self.fields.items():
			css_class = 'form-check-input' if field_name == 'is_private' else 'form-control'
			field.widget.attrs['class'] = css_class
			field.widget.attrs['placeholder'] = ''
			# field.labal = ''
			field.label_suffix = ''
			field.help_text = ''
			field.error_messages = {}

	def as_div(self):
		output = []
		for field in self:
			if field.name == 'password':
				continue
			elif field.name == 'is_private':
				output.append(f'<div class="form-check mb-3">{field}{field.label_tag()}</div>')
			else:
				output.append(f'<div class="form-group mb-3">{field.label_tag()}{field}</div>')
		return mark_safe('\n'.join(output))