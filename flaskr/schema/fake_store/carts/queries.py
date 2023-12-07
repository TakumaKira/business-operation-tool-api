import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import FakeStoreCartType
from .model import FakeStoreCartModel


class FakeStoreCartQuery(graphene.ObjectType):
    fake_store_carts = graphene.List(FakeStoreCartType)
    fake_store_cart_by_id = graphene.Field(FakeStoreCartType, id=graphene.Int(required=True))

    def resolve_fake_store_carts(self, info):
        _fetch_and_store_data()
        return list(FakeStoreCartModel.objects.all())

    def resolve_fake_store_cart_by_id(self, info, id):
        _fetch_and_store_data()
        return FakeStoreCartModel.objects.filter(id=id).first()


def _fetch_and_store_data():
    fetch_and_store_data(f"{BASE_URL}/carts", FakeStoreCartModel, lambda data: data)
