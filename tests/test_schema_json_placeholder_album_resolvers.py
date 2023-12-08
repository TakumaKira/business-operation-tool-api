from graphene.test import Client

from flaskr.schema import schema


def test_resolve_json_placeholder_albums_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderAlbums { id } }''')
    arr = executed.get('data').get('jsonPlaceholderAlbums')
    assert any(item['id'] is not None for item in arr)

def test_resolve_json_placeholder_albums_user_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderAlbums { userId } }''')
    arr = executed.get('data').get('jsonPlaceholderAlbums')
    assert any(item['userId'] is not None for item in arr)

def test_resolve_json_placeholder_albums_title():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderAlbums { title } }''')
    arr = executed.get('data').get('jsonPlaceholderAlbums')
    assert any(item['title'] is not None for item in arr)

def test_resolve_json_placeholder_album_by_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderAlbumById(id:1) { id } }''')
    assert executed == { 'data': { 'jsonPlaceholderAlbumById': { 'id': '1' } } }
