import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonUserType
from .model import DummyJsonUserModel


class DummyJsonUserQuery(graphene.ObjectType):
    dummy_json_users = graphene.List(DummyJsonUserType)

    def resolve_dummy_json_users(self, info):
        fetch_and_store_data(f"{BASE_URL}/users", DummyJsonUserModel, lambda data: data.get('users'))
        return list(DummyJsonUserModel.objects.all())
