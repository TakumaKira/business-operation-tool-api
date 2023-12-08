from graphene.test import Client

from flaskr.schema import schema


def test_resolve_json_placeholder_comments_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderComments { id } }''')
    arr = executed.get('data').get('jsonPlaceholderComments')
    assert any(item['id'] is not None for item in arr)

def test_resolve_json_placeholder_comments_post_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderComments { postId } }''')
    arr = executed.get('data').get('jsonPlaceholderComments')
    assert any(item['postId'] is not None for item in arr)

def test_resolve_json_placeholder_comments_name():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderComments { name } }''')
    arr = executed.get('data').get('jsonPlaceholderComments')
    assert any(item['name'] is not None for item in arr)

def test_resolve_json_placeholder_comments_email():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderComments { email } }''')
    arr = executed.get('data').get('jsonPlaceholderComments')
    assert any(item['email'] is not None for item in arr)

def test_resolve_json_placeholder_comments_body():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderComments { body } }''')
    arr = executed.get('data').get('jsonPlaceholderComments')
    assert any(item['body'] is not None for item in arr)

def test_resolve_json_placeholder_comment_by_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderCommentById(id:1) { id } }''')
    assert executed == { 'data': { 'jsonPlaceholderCommentById': { 'id': '1' } } }
