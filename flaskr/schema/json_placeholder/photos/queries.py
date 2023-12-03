import graphene
from ....data_service import fetch_and_store_data
from .. import BASE_URL
from .type import JsonPlaceholderPhotoType
from .model import JsonPlaceholderPhotoModel


class JsonPlaceholderPhotoQuery(graphene.ObjectType):
    json_placeholder_photos = graphene.List(JsonPlaceholderPhotoType)

    def resolve_json_placeholder_photos(self, info):
        fetch_and_store_data(f"{BASE_URL}/photos", JsonPlaceholderPhotoModel, lambda data: data)
        return list(JsonPlaceholderPhotoModel.objects.all())
