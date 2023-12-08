import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonCommentType
from .model import DummyJsonCommentModel


class DummyJsonCommentQuery(graphene.ObjectType):
    dummy_json_comments = graphene.List(DummyJsonCommentType)
    dummy_json_comment_by_id = graphene.Field(DummyJsonCommentType, id=graphene.Int(required=True))

    def resolve_dummy_json_comments(self, info):
        _fetch_and_store_data()
        return list(DummyJsonCommentModel.objects.all())

    def resolve_dummy_json_comment_by_id(self, info, id):
        _fetch_and_store_data()
        return DummyJsonCommentModel.objects.filter(id=id).first()


URL = f"{BASE_URL}/comments"

def _fetch_and_store_data():
    fetch_and_store_data(URL, DummyJsonCommentModel, lambda data: data.get('comments'))
