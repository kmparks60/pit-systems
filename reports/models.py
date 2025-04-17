from django.db import models
from businesses.models import Business



class Report(models.Model):
	REPORT_TYPE_CHOICES = [
		("inventory", "Inventory"),
		("order_summary", "Order Summary"),
		("stockouts", "Stockouts"),
		("Financial", "Financial"),
		("custom", "Custom"),
	]

	business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='reports')
	report_type = models.CharField(max_length=50, choices=REPORT_TYPE_CHOICES)
	generated_at = models.DateTimeField(auto_now_add=True)
	notes = models.TextField(blank=True)
	file_path = models.CharField(max_length=255, blank=True)
	visible_to_client = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.business.name} - {self.report_type} ({self.generated_at.date()})"