import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import JsonPlaceholderCommentType
from .model import JsonPlaceholderCommentModel


class JsonPlaceholderCommentQuery(graphene.ObjectType):
    json_placeholder_comments = graphene.List(JsonPlaceholderCommentType)
    json_placeholder_comment_by_id = graphene.Field(JsonPlaceholderCommentType, id=graphene.Int(required=True))

    def resolve_json_placeholder_comments(self, info):
        _fetch_and_store_data()
        return list(JsonPlaceholderCommentModel.objects.all())

    def resolve_json_placeholder_comment_by_id(self, info, id):
        _fetch_and_store_data()
        return JsonPlaceholderCommentModel.objects.filter(id=id).first()


def _fetch_and_store_data():
    fetch_and_store_data(f"{BASE_URL}/comments", JsonPlaceholderCommentModel, lambda data: data)
