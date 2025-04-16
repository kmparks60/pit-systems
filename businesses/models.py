from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Business(models.Model):
	BUSINESS_TYPES = [
		("OWNER", "Owner"),
		("CLIENT", "Client"),
		("SUPPLIER", "Supplier"),
		("SHIPPING", "Shipping")
	]

	name = models.CharField(max_length=255)
	address = models.TextField(blank=True)
	shippping_address = models.TextField(blank=True)
	phone_number = models.CharField(max_length=20, blank=True)
	email = models.EmailField(blank=True)
	category = models.CharField(max_length=20, choices=BUSINESS_TYPES)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} ({self.get_category_display()})"
	
class UserManager(BaseUserManager):
	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError("Email is required")
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_superuser(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_staff', True)
		return self.create_user(email, password, **extra_fields)
	
class CustomUser(AbstractBaseUser, PermissionsMixin):
	TIER_CHOICES = [
		("ADMIN", "Admin"),
		("MANAGER", "Manager"),
		("STAFF", "Staff")
	]

	email = models.EmailField(unique=True)
	business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='users')
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	tier = models.CharField(max_length=20, choices=TIER_CHOICES)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'business', 'tier']

	def __str__(self):
		return f"{self.first_name} {self.last_name}({self.email})"