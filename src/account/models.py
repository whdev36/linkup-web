from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
	class Meta:
		verbose_name = 'Account'
		verbose_name_plural = 'Accounts'
	picture = models.ImageField(upload_to='accounts/pictures/', blank=True, null=True)
	bio = models.TextField(max_length=300, blank=True, null=True)
	is_private = models.BooleanField(default=True)
	slug = models.SlugField(unique=True, blank=True, null=True)

	def save(self, *args, **kwargs):
		self.slug = self.slug or self.username
		super().save(*args, **kwargs)
