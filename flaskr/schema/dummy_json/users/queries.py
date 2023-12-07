import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonUserType
from .model import DummyJsonUserModel


class DummyJsonUserQuery(graphene.ObjectType):
    dummy_json_users = graphene.List(DummyJsonUserType)
    dummy_json_user_by_id = graphene.Field(DummyJsonUserType, id=graphene.Int(required=True))

    def resolve_dummy_json_users(self, info):
        _fetch_and_store_data()
        return list(DummyJsonUserModel.objects.all())

    def resolve_dummy_json_user_by_id(self, info, id):
        _fetch_and_store_data()
        return DummyJsonUserModel.objects.filter(id=id).first()


def _fetch_and_store_data():
    fetch_and_store_data(f"{BASE_URL}/users", DummyJsonUserModel, lambda data: data.get('users'))
