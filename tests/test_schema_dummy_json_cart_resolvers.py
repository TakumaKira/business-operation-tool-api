from graphene.test import Client

from flaskr.schema import schema


def test_resolve_dummy_json_carts_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonCarts { id } }''')
    arr = executed.get('data').get('dummyJsonCarts')
    assert any(item['id'] is not None for item in arr)

def test_resolve_dummy_json_carts_user_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonCarts { userId } }''')
    arr = executed.get('data').get('dummyJsonCarts')
    assert any(item['userId'] is not None for item in arr)

def test_resolve_dummy_json_carts_products():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonCarts { products } }''')
    arr = executed.get('data').get('dummyJsonCarts')
    assert any(item['products'] is not None for item in arr)

def test_resolve_dummy_json_carts_discounted_total():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonCarts { discountedTotal } }''')
    arr = executed.get('data').get('dummyJsonCarts')
    assert any(item['discountedTotal'] is not None for item in arr)

def test_resolve_dummy_json_carts_total_products():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonCarts { totalProducts } }''')
    arr = executed.get('data').get('dummyJsonCarts')
    assert any(item['totalProducts'] is not None for item in arr)

def test_resolve_dummy_json_carts_total_quantity():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonCarts { totalQuantity } }''')
    arr = executed.get('data').get('dummyJsonCarts')
    assert any(item['totalQuantity'] is not None for item in arr)

def test_resolve_dummy_json_cart_by_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonCartById(id:1) { id } }''')
    assert executed == { 'data': { 'dummyJsonCartById': { 'id': '1' } } }
