import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import JsonPlaceholderAlbumType
from .model import JsonPlaceholderAlbumModel


class JsonPlaceholderAlbumQuery(graphene.ObjectType):
    json_placeholder_albums = graphene.List(JsonPlaceholderAlbumType)
    json_placeholder_album_by_id = graphene.Field(JsonPlaceholderAlbumType, id=graphene.Int(required=True))

    def resolve_json_placeholder_albums(self, info):
        _fetch_and_store_data()
        return list(JsonPlaceholderAlbumModel.objects.all())

    def resolve_json_placeholder_album_by_id(self, info, id):
        _fetch_and_store_data()
        return JsonPlaceholderAlbumModel.objects.filter(id=id).first()


def _fetch_and_store_data():
    fetch_and_store_data(f"{BASE_URL}/albums", JsonPlaceholderAlbumModel, lambda data: data)
