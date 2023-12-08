from graphene.test import Client

from flaskr.schema import schema


def test_resolve_json_placeholder_users_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderUsers { id } }''')
    arr = executed.get('data').get('jsonPlaceholderUsers')
    assert any(item['id'] is not None for item in arr)

def test_resolve_json_placeholder_users_name():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderUsers { name } }''')
    arr = executed.get('data').get('jsonPlaceholderUsers')
    assert any(item['name'] is not None for item in arr)

def test_resolve_json_placeholder_users_username():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderUsers { username } }''')
    arr = executed.get('data').get('jsonPlaceholderUsers')
    assert any(item['username'] is not None for item in arr)

def test_resolve_json_placeholder_users_email():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderUsers { email } }''')
    arr = executed.get('data').get('jsonPlaceholderUsers')
    assert any(item['email'] is not None for item in arr)

def test_resolve_json_placeholder_users_address():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderUsers { address } }''')
    arr = executed.get('data').get('jsonPlaceholderUsers')
    assert any(item['address'] is not None for item in arr)

def test_resolve_json_placeholder_users_phone():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderUsers { phone } }''')
    arr = executed.get('data').get('jsonPlaceholderUsers')
    assert any(item['phone'] is not None for item in arr)

def test_resolve_json_placeholder_users_website():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderUsers { website } }''')
    arr = executed.get('data').get('jsonPlaceholderUsers')
    assert any(item['website'] is not None for item in arr)

def test_resolve_json_placeholder_users_company():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderUsers { company } }''')
    arr = executed.get('data').get('jsonPlaceholderUsers')
    assert any(item['company'] is not None for item in arr)

def test_resolve_json_placeholder_user_by_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderUserById(id:1) { id } }''')
    assert executed == { 'data': { 'jsonPlaceholderUserById': { 'id': '1' } } }
