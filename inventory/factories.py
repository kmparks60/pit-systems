import factory
import random
from factory.django import DjangoModelFactory
from businesses.factories import BusinessFactory
from inventory.models import Location, Unit
from businesses.models import Business
from django.utils import timezone

class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location

    business = factory.LazyFunction(lambda: random.choice(Business.objects.all()))
    name = factory.Faker('word')
    aisle = factory.LazyFunction(lambda: random.choice(['A1', 'A2', 'A3']))
    shelf = factory.LazyFunction(lambda: random.choice(['S1', 'S2', 'S3']))
    bay = factory.LazyFunction(lambda: random.choice(['B1', 'B2', 'B3']))


class UnitFactory(DjangoModelFactory):
    class Meta:
        model = Unit

    business = factory.LazyAttribute(lambda o: o.location.business if o.location else random.choice(Business.objects.all()))
    location = factory.LazyFunction(lambda: random.choice(Location.objects.all()))
    name = factory.Faker('word')
    description = factory.Faker('sentence')
    received_date = factory.LazyFunction(timezone.now)
    pick_date = factory.LazyFunction(timezone.now)
    exp_date = factory.LazyFunction(lambda: timezone.now() + timezone.timedelta(days=random.randint(30, 365)))
    quantity = factory.Faker('random_int', min=1, max=100)
    unit_price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    taxable = factory.Faker('boolean', chance_of_getting_true=30)

