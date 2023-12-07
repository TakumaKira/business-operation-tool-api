import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import DummyJsonPostType
from .model import DummyJsonPostModel


class DummyJsonPostQuery(graphene.ObjectType):
    dummy_json_posts = graphene.List(DummyJsonPostType)
    dummy_json_post_by_id = graphene.Field(DummyJsonPostType, id=graphene.Int(required=True))

    def resolve_dummy_json_posts(self, info):
        _fetch_and_store_data()
        return list(DummyJsonPostModel.objects.all())

    def resolve_dummy_json_post_by_id(self, info, id):
        _fetch_and_store_data()
        return DummyJsonPostModel.objects.filter(id=id).first()


def _fetch_and_store_data():
    fetch_and_store_data(f"{BASE_URL}/posts", DummyJsonPostModel, lambda data: data.get('posts'))
