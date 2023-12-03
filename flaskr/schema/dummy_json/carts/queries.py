import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonCartType
from .model import DummyJsonCartModel


class DummyJsonCartQuery(graphene.ObjectType):
    dummy_json_carts = graphene.List(DummyJsonCartType)

    def resolve_dummy_json_carts(self, info):
        fetch_and_store_data(f"{BASE_URL}/carts", DummyJsonCartModel, lambda data: data.get('carts'))
        return list(DummyJsonCartModel.objects.all())
