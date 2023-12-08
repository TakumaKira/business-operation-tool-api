from graphene.test import Client

from flaskr.schema import schema


def test_resolve_json_placeholder_posts_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderPosts { id } }''')
    arr = executed.get('data').get('jsonPlaceholderPosts')
    assert any(item['id'] is not None for item in arr)

def test_resolve_json_placeholder_posts_user_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderPosts { userId } }''')
    arr = executed.get('data').get('jsonPlaceholderPosts')
    assert any(item['userId'] is not None for item in arr)

def test_resolve_json_placeholder_posts_title():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderPosts { title } }''')
    arr = executed.get('data').get('jsonPlaceholderPosts')
    assert any(item['title'] is not None for item in arr)

def test_resolve_json_placeholder_posts_body():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderPosts { body } }''')
    arr = executed.get('data').get('jsonPlaceholderPosts')
    assert any(item['body'] is not None for item in arr)

def test_resolve_json_placeholder_post_by_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderPostById(id:1) { id } }''')
    assert executed == { 'data': { 'jsonPlaceholderPostById': { 'id': '1' } } }
