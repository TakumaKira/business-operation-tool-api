from graphene.test import Client

from flaskr.schema import schema


def test_resolve_dummy_json_users_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { id } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['id'] is not None for item in arr)

def test_resolve_dummy_json_users_first_name():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { firstName } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['firstName'] is not None for item in arr)

def test_resolve_dummy_json_users_last_name():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { lastName } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['lastName'] is not None for item in arr)

def test_resolve_dummy_json_users_maiden_name():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { maidenName } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['maidenName'] is not None for item in arr)

def test_resolve_dummy_json_users_age():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { age } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['age'] is not None for item in arr)

def test_resolve_dummy_json_users_gender():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { gender } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['gender'] is not None for item in arr)

def test_resolve_dummy_json_users_email():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { email } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['email'] is not None for item in arr)

def test_resolve_dummy_json_users_phone():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { phone } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['phone'] is not None for item in arr)

def test_resolve_dummy_json_users_username():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { username } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['username'] is not None for item in arr)

# def test_resolve_dummy_json_users_password(): # Should not retrieve password
#     client = Client(schema)
#     executed = client.execute('''{ dummyJsonUsers { password } }''')
#     arr = executed.get('data').get('dummyJsonUsers')
#     assert any(item['password'] is not None for item in arr)

def test_resolve_dummy_json_users_birth_date():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { birthDate } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['birthDate'] is not None for item in arr)

def test_resolve_dummy_json_users_image():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { image } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['image'] is not None for item in arr)

def test_resolve_dummy_json_users_blood_group():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { bloodGroup } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['bloodGroup'] is not None for item in arr)

def test_resolve_dummy_json_users_height():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { height } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['height'] is not None for item in arr)

def test_resolve_dummy_json_users_weight():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { weight } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['weight'] is not None for item in arr)

def test_resolve_dummy_json_users_eye_color():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { eyeColor } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['eyeColor'] is not None for item in arr)

def test_resolve_dummy_json_users_hair():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { hair } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['hair'] is not None for item in arr)

def test_resolve_dummy_json_users_domain():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { domain } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['domain'] is not None for item in arr)

def test_resolve_dummy_json_users_ip():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { ip } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['ip'] is not None for item in arr)

def test_resolve_dummy_json_users_address():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { address } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['address'] is not None for item in arr)

def test_resolve_dummy_json_users_mac_address():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { macAddress } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['macAddress'] is not None for item in arr)

def test_resolve_dummy_json_users_university():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { university } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['university'] is not None for item in arr)

def test_resolve_dummy_json_users_bank():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { bank } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['bank'] is not None for item in arr)

def test_resolve_dummy_json_users_company():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { company } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['company'] is not None for item in arr)

def test_resolve_dummy_json_users_ein():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { ein } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['ein'] is not None for item in arr)

def test_resolve_dummy_json_users_ssn():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { ssn } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['ssn'] is not None for item in arr)

def test_resolve_dummy_json_users_user_agent():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUsers { userAgent } }''')
    arr = executed.get('data').get('dummyJsonUsers')
    assert any(item['userAgent'] is not None for item in arr)

def test_resolve_dummy_json_user_by_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonUserById(id:1) { id } }''')
    assert executed == { 'data': { 'dummyJsonUserById': { 'id': '1' } } }
