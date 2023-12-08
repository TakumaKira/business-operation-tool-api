from graphene.test import Client

from flaskr.schema import schema


def test_resolve_dummy_json_comments_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonComments { id } }''')
    arr = executed.get('data').get('dummyJsonComments')
    assert any(item['id'] is not None for item in arr)

def test_resolve_dummy_json_comments_post_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonComments { postId } }''')
    arr = executed.get('data').get('dummyJsonComments')
    assert any(item['postId'] is not None for item in arr)

def test_resolve_dummy_json_comments_body():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonComments { body } }''')
    arr = executed.get('data').get('dummyJsonComments')
    assert any(item['body'] is not None for item in arr)

def test_resolve_dummy_json_comments_user():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonComments { user } }''')
    arr = executed.get('data').get('dummyJsonComments')
    assert any(item['user'] is not None for item in arr)

def test_resolve_dummy_json_comment_by_id():
    client = Client(schema)
    executed = client.execute('''{ dummyJsonCommentById(id:1) { id } }''')
    assert executed == { 'data': { 'dummyJsonCommentById': { 'id': '1' } } }
