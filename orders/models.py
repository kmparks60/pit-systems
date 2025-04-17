from django.db import models
from businesses.models import Business
from inventory.models import Unit



class Order(models.Model):
	ORDER_TYPE_CHOICES = [
		("incoming", "Incoming"),
		("outgoing", "Outgoing"),
	]

	ORDER_STATUS_CHOICES = [
		("new", "New"),
		("in_process", "In Process"),
		("shipped", "Shipped"),
		("delivered", "Delivered"),
		("returned", "Returned"),
		("stockout", "Stockout"),
		("replacement", "Replacement"),
	]
	
	business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='orders')
	order_type = models.CharField(max_length=20, choices=ORDER_TYPE_CHOICES)
	status = models.CharField(max_length=30, choices=ORDER_STATUS_CHOICES, default='new')
	order_date = models.DateField(auto_now_add=True)
	receiving_company = models.CharField(max_length=255)
	receiving_address = models.TextField()
	sub_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
	payment_type = models.CharField(max_length=50, blank=True)
	taxable = models.BooleanField(default=False)
	order_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Order #{self.id} - {self.business.name}"

class OrderItem(models.Model):
	quantity = models.PositiveIntegerField()
	unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, related_name='order_items')
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
	unit_price = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return f"{self.unit.name} x {self.quantity}"