import requests

from flaskr.schema.dummy_json.carts.queries import URL as DUMMY_JSON_CARTS_URL
from flaskr.schema.dummy_json.comments.queries import URL as DUMMY_JSON_COMMENTS_URL
from flaskr.schema.dummy_json.posts.queries import URL as DUMMY_JSON_POSTS_URL
from flaskr.schema.dummy_json.products.queries import URL as DUMMY_JSON_PRODUCTS_URL
from flaskr.schema.dummy_json.quotes.queries import URL as DUMMY_JSON_QUOTES_URL
from flaskr.schema.dummy_json.todos.queries import URL as DUMMY_JSON_TODOS_URL
from flaskr.schema.dummy_json.users.queries import URL as DUMMY_JSON_USERS_URL

from flaskr.schema.fake_store.carts.queries import URL as FAKE_STORE_CARTS_URL
from flaskr.schema.fake_store.products.queries import URL as FAKE_STORE_PRODUCTS_URL
from flaskr.schema.fake_store.users.queries import URL as FAKE_STORE_USERS_URL

from flaskr.schema.json_placeholder.albums.queries import URL as JSON_PLACEHOLDER_ALBUMS_URL
from flaskr.schema.json_placeholder.comments.queries import URL as JSON_PLACEHOLDER_COMMENTS_URL
from flaskr.schema.json_placeholder.photos.queries import URL as JSON_PLACEHOLDER_PHOTOS_URL
from flaskr.schema.json_placeholder.posts.queries import URL as JSON_PLACEHOLDER_POSTS_URL
from flaskr.schema.json_placeholder.todos.queries import URL as JSON_PLACEHOLDER_TODOS_URL
from flaskr.schema.json_placeholder.users.queries import URL as JSON_PLACEHOLDER_USERS_URL


def test_dummy_json_api_endpoint_validity():
    "Verify DummyJSON API endpoints"
    assert requests.get(DUMMY_JSON_CARTS_URL, timeout=1).status_code == 200
    assert requests.get(DUMMY_JSON_COMMENTS_URL, timeout=1).status_code == 200
    assert requests.get(DUMMY_JSON_POSTS_URL, timeout=1).status_code == 200
    assert requests.get(DUMMY_JSON_PRODUCTS_URL, timeout=1).status_code == 200
    assert requests.get(DUMMY_JSON_QUOTES_URL, timeout=1).status_code == 200
    assert requests.get(DUMMY_JSON_TODOS_URL, timeout=1).status_code == 200
    assert requests.get(DUMMY_JSON_USERS_URL, timeout=1).status_code == 200

def test_fake_store_api_endpoint_validity():
    "Verify Fake Store API endpoints"
    assert requests.get(FAKE_STORE_CARTS_URL, timeout=5).status_code == 200
    assert requests.get(FAKE_STORE_PRODUCTS_URL, timeout=5).status_code == 200
    assert requests.get(FAKE_STORE_USERS_URL, timeout=5).status_code == 200

def test_json_placeholder_api_endpoint_validity():
    "Verify JSON placeholder API endpoints"
    assert requests.get(JSON_PLACEHOLDER_ALBUMS_URL, timeout=1).status_code == 200
    assert requests.get(JSON_PLACEHOLDER_COMMENTS_URL, timeout=1).status_code == 200
    assert requests.get(JSON_PLACEHOLDER_PHOTOS_URL, timeout=1).status_code == 200
    assert requests.get(JSON_PLACEHOLDER_POSTS_URL, timeout=1).status_code == 200
    assert requests.get(JSON_PLACEHOLDER_TODOS_URL, timeout=1).status_code == 200
    assert requests.get(JSON_PLACEHOLDER_USERS_URL, timeout=1).status_code == 200
