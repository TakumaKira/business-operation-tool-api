import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonTodoType
from .model import DummyJsonTodoModel


class DummyJsonTodoQuery(graphene.ObjectType):
    dummy_json_todos = graphene.List(DummyJsonTodoType)
    dummy_json_todo_by_id = graphene.Field(DummyJsonTodoType, id=graphene.Int(required=True))

    def resolve_dummy_json_todos(self, info):
        _fetch_and_store_data()
        return list(DummyJsonTodoModel.objects.all())

    def resolve_dummy_json_todo_by_id(self, info, id):
        _fetch_and_store_data()
        return DummyJsonTodoModel.objects.filter(id=id).first()


URL = f"{BASE_URL}/todos"

def _fetch_and_store_data():
    fetch_and_store_data(URL, DummyJsonTodoModel, lambda data: data.get('todos'))
