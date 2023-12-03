import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonCommentType
from .model import DummyJsonCommentModel


class DummyJsonCommentQuery(graphene.ObjectType):
    dummy_json_comments = graphene.List(DummyJsonCommentType)

    def resolve_dummy_json_comments(self, info):
        fetch_and_store_data(f"{BASE_URL}/comments", DummyJsonCommentModel, lambda data: data.get('comments'))
        return list(DummyJsonCommentModel.objects.all())
