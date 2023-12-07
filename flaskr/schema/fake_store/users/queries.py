import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import FakeStoreUserType
from .model import FakeStoreUserModel


class FakeStoreUserQuery(graphene.ObjectType):
    fake_store_users = graphene.List(FakeStoreUserType)
    fake_store_user_by_id = graphene.Field(FakeStoreUserType, id=graphene.Int(required=True))

    def resolve_fake_store_users(self, info):
        _fetch_and_store_data()
        return list(FakeStoreUserModel.objects.all())

    def resolve_fake_store_user_by_id(self, info, id):
        _fetch_and_store_data()
        return FakeStoreUserModel.objects.filter(id=id).first()


def _fetch_and_store_data():
    fetch_and_store_data(f"{BASE_URL}/users", FakeStoreUserModel, lambda data: data)
