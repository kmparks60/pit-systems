from django.db import models
from businesses.models import Business
from orders.models import Order
from inventory.models import Location



class Shipment(models.Model):
	SHIPMENT_STATUS_CHOICES = [
		("pending", "Pending"),
		("in_transit", "In Transit"),
		("delayed", "Delayed"),
		("delivered", "Delivered"),
		("failed", "Failed"),
	]
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='shipments')
	shipper = models.ForeignKey(Business, on_delete=models.SET_NULL, null=True, related_name='shipments_sent')
	recipient = models.ForeignKey(Business, on_delete=models.SET_NULL, null=True, related_name='shipments_received')
	tracking_number = models.CharField(max_length=100, blank=True, null=True)
	origin = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='shipments_origin')
	destination = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='shipments_destination')
	status = models.CharField(max_length=50, choices=SHIPMENT_STATUS_CHOICES, default='pending')
	estimated_arrival = models.DateField(null=True, blank=True)
	delivered_on = models.DateField(null=True, blank=True)
	created_at = models.DateField(auto_now_add=True)

	def __str__(self):
		return f"Shipment ${self.id} - {self.status}"