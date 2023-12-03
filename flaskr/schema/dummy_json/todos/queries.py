import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonTodoType
from .model import DummyJsonTodoModel


class DummyJsonTodoQuery(graphene.ObjectType):
    dummy_json_todos = graphene.List(DummyJsonTodoType)

    def resolve_dummy_json_todos(self, info):
        fetch_and_store_data(f"{BASE_URL}/todos", DummyJsonTodoModel, lambda data: data.get('todos'))
        return list(DummyJsonTodoModel.objects.all())
