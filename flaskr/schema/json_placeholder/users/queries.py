import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import JsonPlaceholderUserType
from .model import JsonPlaceholderUserModel


class JsonPlaceholderUserQuery(graphene.ObjectType):
    json_placeholder_users = graphene.List(JsonPlaceholderUserType)

    def resolve_json_placeholder_users(self, info):
        fetch_and_store_data(f"{BASE_URL}/users", JsonPlaceholderUserModel, lambda data: data)
        return list(JsonPlaceholderUserModel.objects.all())
