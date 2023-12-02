import graphene

from .dummy_json.users.queries import DummyJsonUserQuery
from .fake_store.carts.queries import FakeStoreCartQuery
from .fake_store.products.queries import FakeStoreProductQuery
from .fake_store.users.queries import FakeStoreUserQuery
from .json_placeholder.users.queries import JsonPlaceholderUserQuery


class Query(
    DummyJsonUserQuery,
    FakeStoreCartQuery,
    FakeStoreProductQuery,
    FakeStoreUserQuery,
    JsonPlaceholderUserQuery,
    graphene.ObjectType
):
    # This class will inherit from multiple Queries related to different services
    pass


schema = graphene.Schema(query=Query)
