import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonProductType
from .model import DummyJsonProductModel


class DummyJsonProductQuery(graphene.ObjectType):
    dummy_json_products = graphene.List(DummyJsonProductType)
    dummy_json_product_by_id = graphene.Field(DummyJsonProductType, id=graphene.Int(required=True))

    def resolve_dummy_json_products(self, info):
        _fetch_and_store_data()
        return list(DummyJsonProductModel.objects.all())

    def resolve_dummy_json_product_by_id(self, info, id):
        _fetch_and_store_data()
        return DummyJsonProductModel.objects.filter(id=id).first()


URL = f"{BASE_URL}/products"

def _fetch_and_store_data():
    fetch_and_store_data(URL, DummyJsonProductModel, lambda data: data.get('products'))
