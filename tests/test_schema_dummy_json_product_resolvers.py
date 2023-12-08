from graphene.test import Client

from flaskr.schema import schema


def test_resolve_dummy_json_products_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonProducts { id } }''')
    arr = executed.get('data').get('dummyJsonProducts')
    assert any(item['id'] is not None for item in arr)

def test_resolve_dummy_json_products_title():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonProducts { title } }''')
    arr = executed.get('data').get('dummyJsonProducts')
    assert any(item['title'] is not None for item in arr)

def test_resolve_dummy_json_products_description():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonProducts { description } }''')
    arr = executed.get('data').get('dummyJsonProducts')
    assert any(item['description'] is not None for item in arr)

def test_resolve_dummy_json_products_price():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonProducts { price } }''')
    arr = executed.get('data').get('dummyJsonProducts')
    assert any(item['price'] is not None for item in arr)

def test_resolve_dummy_json_products_discount_percentage():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonProducts { discountPercentage } }''')
    arr = executed.get('data').get('dummyJsonProducts')
    assert any(item['discountPercentage'] is not None for item in arr)

def test_resolve_dummy_json_products_rating():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonProducts { rating } }''')
    arr = executed.get('data').get('dummyJsonProducts')
    assert any(item['rating'] is not None for item in arr)

def test_resolve_dummy_json_products_stock():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonProducts { stock } }''')
    arr = executed.get('data').get('dummyJsonProducts')
    assert any(item['stock'] is not None for item in arr)

def test_resolve_dummy_json_products_brand():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonProducts { brand } }''')
    arr = executed.get('data').get('dummyJsonProducts')
    assert any(item['brand'] is not None for item in arr)

def test_resolve_dummy_json_products_category():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonProducts { category } }''')
    arr = executed.get('data').get('dummyJsonProducts')
    assert any(item['category'] is not None for item in arr)

def test_resolve_dummy_json_products_thumbnail():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonProducts { thumbnail } }''')
    arr = executed.get('data').get('dummyJsonProducts')
    assert any(item['thumbnail'] is not None for item in arr)

def test_resolve_dummy_json_products_images():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonProducts { images } }''')
    arr = executed.get('data').get('dummyJsonProducts')
    assert any(item['images'] is not None for item in arr)

def test_resolve_dummy_json_product_by_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonProductById(id:1) { id } }''')
    assert executed == { 'data': { 'dummyJsonProductById': { 'id': '1' } } }
