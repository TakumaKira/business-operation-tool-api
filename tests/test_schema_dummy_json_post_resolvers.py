from graphene.test import Client

from flaskr.schema import schema


def test_resolve_dummy_json_posts_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonPosts { id } }''')
    arr = executed.get('data').get('dummyJsonPosts')
    assert any(item['id'] is not None for item in arr)

def test_resolve_dummy_json_posts_user_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonPosts { userId } }''')
    arr = executed.get('data').get('dummyJsonPosts')
    assert any(item['userId'] is not None for item in arr)

def test_resolve_dummy_json_posts_title():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonPosts { title } }''')
    arr = executed.get('data').get('dummyJsonPosts')
    assert any(item['title'] is not None for item in arr)

def test_resolve_dummy_json_posts_body():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonPosts { body } }''')
    arr = executed.get('data').get('dummyJsonPosts')
    assert any(item['body'] is not None for item in arr)

def test_resolve_dummy_json_posts_tags():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonPosts { tags } }''')
    arr = executed.get('data').get('dummyJsonPosts')
    assert any(item['tags'] is not None for item in arr)

def test_resolve_dummy_json_posts_reactions():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonPosts { reactions } }''')
    arr = executed.get('data').get('dummyJsonPosts')
    assert any(item['reactions'] is not None for item in arr)

def test_resolve_dummy_json_post_by_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonPostById(id:1) { id } }''')
    assert executed == { 'data': { 'dummyJsonPostById': { 'id': '1' } } }
