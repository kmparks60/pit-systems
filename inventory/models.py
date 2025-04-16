from django.db import models
from businesses.models import Business


class Location(models.Model):
	AISLE_CHOICES = [
		('A1', 'Aisle 1'),
		('A2', 'Aisle 2'),
		('A3', 'Aisle 3')
	]

	SHELF_CHOICES = [
		('S1', 'Shelf 1'),
		('S2', 'Shelf 2'),
		('S3', 'Shelf 3')
	]

	BAY_CHOICES = [
		('B1', 'Bay 1'),
		('B2', 'Bay 2'),
		('B3', 'Bay 3')
	]

	business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='locations')
	name = models.CharField(max_length=150)
	aisle = models.CharField(max_length=2, choices=AISLE_CHOICES)
	shelf = models.CharField(max_length=2, choices=SHELF_CHOICES)
	bay = models.CharField(max_length=2, choices=BAY_CHOICES)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.business.name} - {self.name} (Aisle {self.aisle}, Shelf {self.shelf}, Bay {self.bay})"

class Unit(models.Model):
	UNIT_TYPE_CHOICES = [
        ('perishable', 'Perishable'),
        ('non_perishable', 'Non-Perishable'),
        ('hazardous', 'Hazardous'),
		('non-hazardous', 'Non-Hazardous')
    ]

	business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='units')
	name = models.CharField(max_length=150)
	description = models.TextField(blank=True)
	unit_type = models.CharField(max_length=50, choices=UNIT_TYPE_CHOICES)
	location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='units')
	received_date = models.DateField()
	pick_date = models.DateField(null=True, blank=True)
	exp_date = models.DateField(null=True, blank=True)
	quantity = models.PositiveIntegerField()
	unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	taxable = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} ({self.quantity})"
