from graphene.test import Client

from flaskr.schema import schema


def test_resolve_fake_store_products_id():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreProducts { id } }''')
    arr = executed.get('data').get('fakeStoreProducts')
    assert any(item['id'] is not None for item in arr)

def test_resolve_fake_store_products_title():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreProducts { title } }''')
    arr = executed.get('data').get('fakeStoreProducts')
    assert any(item['title'] is not None for item in arr)

def test_resolve_fake_store_products_price():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreProducts { price } }''')
    arr = executed.get('data').get('fakeStoreProducts')
    assert any(item['price'] is not None for item in arr)

def test_resolve_fake_store_products_description():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreProducts { description } }''')
    arr = executed.get('data').get('fakeStoreProducts')
    assert any(item['description'] is not None for item in arr)

def test_resolve_fake_store_products_category():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreProducts { category } }''')
    arr = executed.get('data').get('fakeStoreProducts')
    assert any(item['category'] is not None for item in arr)

def test_resolve_fake_store_products_image():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreProducts { image } }''')
    arr = executed.get('data').get('fakeStoreProducts')
    assert any(item['image'] is not None for item in arr)

def test_resolve_fake_store_products_rating():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreProducts { rating } }''')
    arr = executed.get('data').get('fakeStoreProducts')
    assert any(item['rating'] is not None for item in arr)

def test_resolve_fake_store_product_by_id():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreProductById(id:1) { id } }''')
    assert executed == { 'data': { 'fakeStoreProductById': { 'id': '1' } } }
