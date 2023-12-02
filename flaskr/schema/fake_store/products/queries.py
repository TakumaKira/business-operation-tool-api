import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import FakeStoreProductType
from .model import FakeStoreProductModel


class FakeStoreProductQuery(graphene.ObjectType):
    fake_store_products = graphene.List(FakeStoreProductType)

    def resolve_fake_store_products(self, info):
        fetch_and_store_data(f"{BASE_URL}/products", FakeStoreProductModel)
        return list(FakeStoreProductModel.objects.all())
