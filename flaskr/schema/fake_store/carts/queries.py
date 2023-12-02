import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import FakeStoreCartType
from .model import FakeStoreCartModel


class FakeStoreCartQuery(graphene.ObjectType):
    fake_store_carts = graphene.List(FakeStoreCartType)

    def resolve_fake_store_carts(self, info):
        fetch_and_store_data(f"{BASE_URL}/carts", FakeStoreCartModel, lambda data: data)
        return list(FakeStoreCartModel.objects.all())
