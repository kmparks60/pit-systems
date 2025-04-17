import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory
from businesses.models import Business

User = get_user_model()

class BusinessFactory(DjangoModelFactory):
    class Meta:
        model = Business

    name = factory.Faker('company')
    category = factory.Iterator(['CLIENT', 'CLIENT', 'CLIENT', 'SHIPPING', 'SUPPLIER'])
    tier = factory.Iterator(['BASE', 'SILVER', 'GOLD', 'BASE', 'BASE']) 

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = factory.LazyAttribute(lambda obj: f"{obj.first_name.lower()}.{obj.last_name.lower()}@example.com")
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    tier = factory.Iterator(['MANAGER', 'STAFF', 'STAFF'])
    is_staff = False
    is_superuser = False
    business = factory.SubFactory(BusinessFactory)

    @factory.post_generation
    def password(obj, create, extracted, **kwargs):
        pw = extracted if extracted else 'password123'
        obj.set_password(pw)
        if create:
            obj.save()
