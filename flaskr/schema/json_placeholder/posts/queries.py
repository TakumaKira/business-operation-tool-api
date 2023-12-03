import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import JsonPlaceholderPostType
from .model import JsonPlaceholderPostModel


class JsonPlaceholderPostQuery(graphene.ObjectType):
    json_placeholder_posts = graphene.List(JsonPlaceholderPostType)

    def resolve_json_placeholder_posts(self, info):
        fetch_and_store_data(f"{BASE_URL}/posts", JsonPlaceholderPostModel, lambda data: data)
        return list(JsonPlaceholderPostModel.objects.all())
