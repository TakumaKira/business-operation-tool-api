import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import JsonPlaceholderPostType
from .model import JsonPlaceholderPostModel


class JsonPlaceholderPostQuery(graphene.ObjectType):
    json_placeholder_posts = graphene.List(JsonPlaceholderPostType)
    json_placeholder_post_by_id = graphene.Field(JsonPlaceholderPostType, id=graphene.Int(required=True))

    def resolve_json_placeholder_posts(self, info):
        _fetch_and_store_data()
        return list(JsonPlaceholderPostModel.objects.all())

    def resolve_json_placeholder_post_by_id(self, info, id):
        _fetch_and_store_data()
        return JsonPlaceholderPostModel.objects.filter(id=id).first()


URL = f"{BASE_URL}/posts"

def _fetch_and_store_data():
    fetch_and_store_data(URL, JsonPlaceholderPostModel, lambda data: data)
