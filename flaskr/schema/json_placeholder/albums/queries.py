import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import JsonPlaceholderAlbumType
from .model import JsonPlaceholderAlbumModel


class JsonPlaceholderAlbumQuery(graphene.ObjectType):
    json_placeholder_albums = graphene.List(JsonPlaceholderAlbumType)

    def resolve_json_placeholder_albums(self, info):
        fetch_and_store_data(f"{BASE_URL}/albums", JsonPlaceholderAlbumModel, lambda data: data)
        return list(JsonPlaceholderAlbumModel.objects.all())
