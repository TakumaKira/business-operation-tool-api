import graphene

from .fake_store.carts.queries import FakeStoreCartQuery
from .fake_store.products.queries import FakeStoreProductQuery
from .fake_store.users.queries import FakeStoreUserQuery


class Query(
    FakeStoreCartQuery,
    FakeStoreProductQuery,
    FakeStoreUserQuery,
    graphene.ObjectType
):
    # This class will inherit from multiple Queries related to different services
    pass


schema = graphene.Schema(query=Query)
