from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



# Create your models here.

class UserProfileManager(BaseUserManager):
	"""helps django work with our custom user model"""
	def create_user(self,email,name,password=None):
		"""create a new user profile object"""

		if not email:
			raise ValueError("user must have an email address")

		email=self.normalize_email(email)
		user=self.model(email=email,name=name)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self,email,name,password):
		"""creates and saves a new superuser with given details"""

		user=self.create_user(email,name,password)

		user.is_superuser=True
		user.is_staff=True

		user.save(using=self._db)



class UserProfile(AbstractBaseUser,PermissionsMixin):
	"""Represents the user profile inside our system"""

	email=models.EmailField(max_length=255,unique=True)
	name=models.CharField(max_length=255)
	is_active=models.BooleanField(default=True)
	is_staff=models.BooleanField(default=False)

	objects=UserProfileManager()

	USERNAME_FIELD="email"
	REQUIRED_FIELDS=['name']

	def get_full_name(self):
		"""Used to get a users full name"""

		return self.name


	def get_short_name(self):
		"""used to get a user short name"""

		return self.name


	def __str__(self):
		"""django uses this when it need to convert the objects to a string"""

		return self.email


class ProfileFeedItem(models.Model):
	""""profile status update"""
	user_profile=models.ForeignKey('UserProfile',on_delete=models.CASCADE)
	status_text=models.CharField(max_length=255)
	created_on=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""returns the models as a string"""
		return self.status_text
