import graphene
from .type import FakeStoreProductType
from .model import FakeStoreProductModel

class FakeStoreProductQuery(graphene.ObjectType):
    fake_store_products = graphene.List(FakeStoreProductType)

    def resolve_fake_store_products(self, info):
      return list(FakeStoreProductModel.objects.all())
