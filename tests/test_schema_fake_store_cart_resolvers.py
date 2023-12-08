from graphene.test import Client

from flaskr.schema import schema


def test_resolve_fake_store_carts_id():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreCarts { id } }''')
    arr = executed.get('data').get('fakeStoreCarts')
    assert any(item['id'] is not None for item in arr)

def test_resolve_fake_store_carts_user_id():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreCarts { userId } }''')
    arr = executed.get('data').get('fakeStoreCarts')
    assert any(item['userId'] is not None for item in arr)

def test_resolve_fake_store_carts_date():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreCarts { date } }''')
    arr = executed.get('data').get('fakeStoreCarts')
    assert any(item['date'] is not None for item in arr)

def test_resolve_fake_store_carts_products():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreCarts { products } }''')
    arr = executed.get('data').get('fakeStoreCarts')
    assert any(item['products'] is not None for item in arr)

def test_resolve_fake_store_cart_by_id():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreCartById(id:1) { id } }''')
    assert executed == { 'data': { 'fakeStoreCartById': { 'id': '1' } } }
