import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import JsonPlaceholderTodoType
from .model import JsonPlaceholderTodoModel


class JsonPlaceholderTodoQuery(graphene.ObjectType):
    json_placeholder_todos = graphene.List(JsonPlaceholderTodoType)
    json_placeholder_todo_by_id = graphene.Field(JsonPlaceholderTodoType, id=graphene.Int(required=True))

    def resolve_json_placeholder_todos(self, info):
        _fetch_and_store_data()
        return list(JsonPlaceholderTodoModel.objects.all())

    def resolve_json_placeholder_todo_by_id(self, info, id):
        _fetch_and_store_data()
        return JsonPlaceholderTodoModel.objects.filter(id=id).first()


URL = f"{BASE_URL}/todos"

def _fetch_and_store_data():
    fetch_and_store_data(URL, JsonPlaceholderTodoModel, lambda data: data)
