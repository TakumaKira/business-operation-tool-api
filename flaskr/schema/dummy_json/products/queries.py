import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonProductType
from .model import DummyJsonProductModel


class DummyJsonProductQuery(graphene.ObjectType):
    dummy_json_products = graphene.List(DummyJsonProductType)

    def resolve_dummy_json_products(self, info):
        fetch_and_store_data(f"{BASE_URL}/products", DummyJsonProductModel, lambda data: data.get('products'))
        return list(DummyJsonProductModel.objects.all())
