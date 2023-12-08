import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonCartType
from .model import DummyJsonCartModel


class DummyJsonCartQuery(graphene.ObjectType):
    dummy_json_carts = graphene.List(DummyJsonCartType)
    dummy_json_cart_by_id = graphene.Field(DummyJsonCartType, id=graphene.Int(required=True))

    def resolve_dummy_json_carts(self, info):
        _fetch_and_store_data()
        return list(DummyJsonCartModel.objects.all())

    def resolve_dummy_json_cart_by_id(self, info, id):
        _fetch_and_store_data()
        return DummyJsonCartModel.objects.filter(id=id).first()


URL = f"{BASE_URL}/carts"

def _fetch_and_store_data():
    fetch_and_store_data(URL, DummyJsonCartModel, lambda data: data.get('carts'))
