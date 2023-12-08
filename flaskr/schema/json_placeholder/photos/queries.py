import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import JsonPlaceholderPhotoType
from .model import JsonPlaceholderPhotoModel


class JsonPlaceholderPhotoQuery(graphene.ObjectType):
    json_placeholder_photos = graphene.List(JsonPlaceholderPhotoType)
    json_placeholder_photo_by_id = graphene.Field(JsonPlaceholderPhotoType, id=graphene.Int(required=True))

    def resolve_json_placeholder_photos(self, info):
        _fetch_and_store_data()
        return list(JsonPlaceholderPhotoModel.objects.all())

    def resolve_json_placeholder_photo_by_id(self, info, id):
        _fetch_and_store_data()
        return JsonPlaceholderPhotoModel.objects.filter(id=id).first()


URL = f"{BASE_URL}/photos"

def _fetch_and_store_data():
    fetch_and_store_data(URL, JsonPlaceholderPhotoModel, lambda data: data)
