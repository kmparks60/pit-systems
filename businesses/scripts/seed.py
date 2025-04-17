from businesses.factories import BusinessFactory, UserFactory

def run():
    for tier in ['BASE', 'SILVER', 'GOLD']:
        client = BusinessFactory(category='CLIENT', tier=tier)
        print(f"Created Client Business: {client.name} ({tier})")
        for _ in range(3):
            user = UserFactory(business=client)
            print(f"  - User: {user.email}")

    shipping = BusinessFactory(category='shipping', tier=None)
    print(f"Created Shipping Business: {shipping.name}")

    supplier = BusinessFactory(category='supplier', tier=None)
    print(f"Created Supplier Business: {supplier.name}")
