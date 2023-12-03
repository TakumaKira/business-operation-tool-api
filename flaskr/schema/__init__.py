import graphene

from .dummy_json.carts.queries import DummyJsonCartQuery
from .dummy_json.comments.queries import DummyJsonCommentQuery
from .dummy_json.posts.queries import DummyJsonPostQuery
from .dummy_json.products.queries import DummyJsonProductQuery
from .dummy_json.quotes.queries import DummyJsonQuoteQuery
from .dummy_json.todos.queries import DummyJsonTodoQuery
from .dummy_json.users.queries import DummyJsonUserQuery

from .fake_store.carts.queries import FakeStoreCartQuery
from .fake_store.products.queries import FakeStoreProductQuery
from .fake_store.users.queries import FakeStoreUserQuery

from .json_placeholder.albums.queries import JsonPlaceholderAlbumQuery
from .json_placeholder.comments.queries import JsonPlaceholderCommentQuery
from .json_placeholder.photos.queries import JsonPlaceholderPhotoQuery
from .json_placeholder.posts.queries import JsonPlaceholderPostQuery
from .json_placeholder.todos.queries import JsonPlaceholderTodoQuery
from .json_placeholder.users.queries import JsonPlaceholderUserQuery


class Query(
    DummyJsonCartQuery,
    DummyJsonCommentQuery,
    DummyJsonPostQuery,
    DummyJsonProductQuery,
    DummyJsonQuoteQuery,
    DummyJsonTodoQuery,
    DummyJsonUserQuery,

    FakeStoreCartQuery,
    FakeStoreProductQuery,
    FakeStoreUserQuery,

    JsonPlaceholderAlbumQuery,
    JsonPlaceholderCommentQuery,
    JsonPlaceholderPhotoQuery,
    JsonPlaceholderPostQuery,
    JsonPlaceholderTodoQuery,
    JsonPlaceholderUserQuery,

    graphene.ObjectType
):
    # This class will inherit from multiple Queries related to different services
    pass


schema = graphene.Schema(query=Query)
