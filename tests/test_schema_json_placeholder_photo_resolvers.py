from graphene.test import Client

from flaskr.schema import schema


def test_resolve_json_placeholder_photos_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderPhotos { id } }''')
    arr = executed.get('data').get('jsonPlaceholderPhotos')
    assert any(item['id'] is not None for item in arr)

def test_resolve_json_placeholder_photos_album_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderPhotos { albumId } }''')
    arr = executed.get('data').get('jsonPlaceholderPhotos')
    assert any(item['albumId'] is not None for item in arr)

def test_resolve_json_placeholder_photos_title():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderPhotos { title } }''')
    arr = executed.get('data').get('jsonPlaceholderPhotos')
    assert any(item['title'] is not None for item in arr)

def test_resolve_json_placeholder_photos_url():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderPhotos { url } }''')
    arr = executed.get('data').get('jsonPlaceholderPhotos')
    assert any(item['url'] is not None for item in arr)

def test_resolve_json_placeholder_photos_thumbnail_url():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderPhotos { thumbnailUrl } }''')
    arr = executed.get('data').get('jsonPlaceholderPhotos')
    assert any(item['thumbnailUrl'] is not None for item in arr)

def test_resolve_json_placeholder_photo_by_id():
    client = Client(schema)
    executed = client.execute('''{ jsonPlaceholderPhotoById(id:1) { id } }''')
    assert executed == { 'data': { 'jsonPlaceholderPhotoById': { 'id': '1' } } }
