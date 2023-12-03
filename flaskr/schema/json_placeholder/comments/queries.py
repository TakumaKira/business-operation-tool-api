import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import JsonPlaceholderCommentType
from .model import JsonPlaceholderCommentModel


class JsonPlaceholderCommentQuery(graphene.ObjectType):
    json_placeholder_comments = graphene.List(JsonPlaceholderCommentType)

    def resolve_json_placeholder_comments(self, info):
        fetch_and_store_data(f"{BASE_URL}/comments", JsonPlaceholderCommentModel, lambda data: data)
        return list(JsonPlaceholderCommentModel.objects.all())
