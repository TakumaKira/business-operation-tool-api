import graphene

from .fake_store.products.queries import FakeStoreProductQuery


class Query(FakeStoreProductQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries related to different services
    pass


schema = graphene.Schema(query=Query)
