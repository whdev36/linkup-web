# forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django.utils.safestring import mark_safe

class AccountForm(UserCreationForm):
	class Meta:
		model = Account
		fields = ['email', 'first_name', 'last_name', 'username',  'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = ''
			# field.widget.attrs['placeholder'] = ''
			# field.label = ''
			field.label_suffix = ''
			field.help_text = ''
			field.error_messages = {}

	def as_div(self):
		output = []
		for field in self:
			output.append(f'<div>{field.label_tag()}{field}</div>')
		return mark_safe('\n'.join(output))