import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import FakeStoreUserType
from .model import FakeStoreUserModel


class FakeStoreUserQuery(graphene.ObjectType):
    fake_store_users = graphene.List(FakeStoreUserType)

    def resolve_fake_store_users(self, info):
        fetch_and_store_data(f"{BASE_URL}/users", FakeStoreUserModel)
        return list(FakeStoreUserModel.objects.all())
