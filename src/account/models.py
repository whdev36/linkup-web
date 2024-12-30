from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
	# Color choices
	COLOR_CHOICE = [
		('primary', 'Primary'),
		('secondary', 'Secondary'),
		('success', 'Success'),
		('info', 'Info'),
		('danger', 'Danger'),
		('warning', 'Warning'),
		('dark', 'Dark'),
	]

	class Meta:
		verbose_name = 'Account'
		verbose_name_plural = 'Accounts'
	picture = models.ImageField(upload_to='accounts/pictures/', blank=True, null=True)
	bio = models.TextField(max_length=300, blank=True, null=True)
	is_private = models.BooleanField(default=True)
	slug = models.SlugField(unique=True, blank=True, null=True)
	follows = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='followers')
	color = models.CharField(max_length=12, choices=COLOR_CHOICE, default='secondary', blank=True, null=True)

	def save(self, *args, **kwargs):
		self.slug = self.slug or self.username
		super().save(*args, **kwargs)
