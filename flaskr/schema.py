import graphene

from graphene_mongo import MongoengineObjectType

from .models import FakeStoreProduct as FakeStoreProductModel


class FakeStoreProduct(MongoengineObjectType):
    class Meta:
        model = FakeStoreProductModel


class Query(graphene.ObjectType):
    fake_store_products = graphene.List(FakeStoreProduct, description='Products from Fake Store API')

    def resolve_fake_store_products(self, info):
        return list(FakeStoreProductModel.objects.all())


schema = graphene.Schema(query=Query)
