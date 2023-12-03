import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonPostType
from .model import DummyJsonPostModel


class DummyJsonPostQuery(graphene.ObjectType):
    dummy_json_posts = graphene.List(DummyJsonPostType)

    def resolve_dummy_json_posts(self, info):
        fetch_and_store_data(f"{BASE_URL}/posts", DummyJsonPostModel, lambda data: data.get('posts'))
        return list(DummyJsonPostModel.objects.all())
