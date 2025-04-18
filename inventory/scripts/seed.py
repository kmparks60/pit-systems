from businesses.models import Business
from inventory.models import Location
from inventory.factories import LocationFactory, UnitFactory

def run():
    if not Business.objects.exists():
        print("Please seed businesses first.")
        return

    for business in Business.objects.all():
        LocationFactory.create_batch(5, business=business)

    if not Location.objects.exists():
        print("No locations found to seed units.")
        return

    for location in Location.objects.all():
        UnitFactory.create_batch(10, location=location)
