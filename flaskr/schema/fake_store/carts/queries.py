import graphene
from ....data_service import fetch_and_store_data
from .type import FakeStoreCartType
from .model import FakeStoreCartModel


class FakeStoreCartQuery(graphene.ObjectType):
    fake_store_carts = graphene.List(FakeStoreCartType)

    def resolve_fake_store_carts(self, info):
        fetch_and_store_data("https://fakestoreapi.com/carts", FakeStoreCartModel)
        return list(FakeStoreCartModel.objects.all())
