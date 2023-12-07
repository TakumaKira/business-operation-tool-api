import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import FakeStoreProductType
from .model import FakeStoreProductModel


class FakeStoreProductQuery(graphene.ObjectType):
    fake_store_products = graphene.List(FakeStoreProductType)
    fake_store_product_by_id = graphene.Field(FakeStoreProductType, id=graphene.Int(required=True))

    def resolve_fake_store_products(self, info):
        _fetch_and_store_data()
        return list(FakeStoreProductModel.objects.all())

    def resolve_fake_store_product_by_id(self, info, id):
        _fetch_and_store_data()
        return FakeStoreProductModel.objects.filter(id=id).first()


def _fetch_and_store_data():
    fetch_and_store_data(f"{BASE_URL}/products", FakeStoreProductModel, lambda data: data)
