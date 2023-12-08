from graphene.test import Client

from flaskr.schema import schema


def test_resolve_fake_store_users_id():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreUsers { id } }''')
    arr = executed.get('data').get('fakeStoreUsers')
    assert any(item['id'] is not None for item in arr)

def test_resolve_fake_store_users_address():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreUsers { address } }''')
    arr = executed.get('data').get('fakeStoreUsers')
    assert any(item['address'] is not None for item in arr)

def test_resolve_fake_store_users_email():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreUsers { email } }''')
    arr = executed.get('data').get('fakeStoreUsers')
    assert any(item['email'] is not None for item in arr)

def test_resolve_fake_store_users_username():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreUsers { username } }''')
    arr = executed.get('data').get('fakeStoreUsers')
    assert any(item['username'] is not None for item in arr)

# def test_resolve_fake_store_users_password(): # Should not retrieve password
#     client = Client(schema)
#     executed = client.execute('''{ fakeStoreUsers { password } }''')
#     arr = executed.get('data').get('fakeStoreUsers')
#     assert any(item['password'] is not None for item in arr)

def test_resolve_fake_store_users_name():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreUsers { name } }''')
    arr = executed.get('data').get('fakeStoreUsers')
    assert any(item['name'] is not None for item in arr)

def test_resolve_fake_store_users_phone():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreUsers { phone } }''')
    arr = executed.get('data').get('fakeStoreUsers')
    assert any(item['phone'] is not None for item in arr)

def test_resolve_fake_store_user_by_id():
    client = Client(schema)
    executed = client.execute('''{ fakeStoreUserById(id:1) { id } }''')
    assert executed == { 'data': { 'fakeStoreUserById': { 'id': '1' } } }
