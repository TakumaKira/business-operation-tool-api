import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import JsonPlaceholderTodoType
from .model import JsonPlaceholderTodoModel


class JsonPlaceholderTodoQuery(graphene.ObjectType):
    json_placeholder_todos = graphene.List(JsonPlaceholderTodoType)

    def resolve_json_placeholder_todos(self, info):
        fetch_and_store_data(f"{BASE_URL}/todos", JsonPlaceholderTodoModel, lambda data: data)
        return list(JsonPlaceholderTodoModel.objects.all())
