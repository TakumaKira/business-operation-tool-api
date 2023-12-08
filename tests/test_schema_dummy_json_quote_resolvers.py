from graphene.test import Client

from flaskr.schema import schema


def test_resolve_dummy_json_quotes_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonQuotes { id } }''')
    arr = executed.get('data').get('dummyJsonQuotes')
    assert any(item['id'] is not None for item in arr)

def test_resolve_dummy_json_quotes_quote():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonQuotes { quote } }''')
    arr = executed.get('data').get('dummyJsonQuotes')
    assert any(item['quote'] is not None for item in arr)

def test_resolve_dummy_json_quotes_author():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonQuotes { author } }''')
    arr = executed.get('data').get('dummyJsonQuotes')
    assert any(item['author'] is not None for item in arr)

def test_resolve_dummy_json_quote_by_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonQuoteById(id:1) { id } }''')
    assert executed == { 'data': { 'dummyJsonQuoteById': { 'id': '1' } } }
