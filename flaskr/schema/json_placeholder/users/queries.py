import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import JsonPlaceholderUserType
from .model import JsonPlaceholderUserModel


class JsonPlaceholderUserQuery(graphene.ObjectType):
    json_placeholder_users = graphene.List(JsonPlaceholderUserType)
    json_placeholder_user_by_id = graphene.Field(JsonPlaceholderUserType, id=graphene.Int(required=True))

    def resolve_json_placeholder_users(self, info):
        _fetch_and_store_data()
        return list(JsonPlaceholderUserModel.objects.all())

    def resolve_json_placeholder_user_by_id(self, info, id):
        _fetch_and_store_data()
        return JsonPlaceholderUserModel.objects.filter(id=id).first()


URL = f"{BASE_URL}/users"

def _fetch_and_store_data():
    fetch_and_store_data(URL, JsonPlaceholderUserModel, lambda data: data)
