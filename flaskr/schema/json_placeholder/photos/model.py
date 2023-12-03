from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class JsonPlaceholderPhotoModel(Document):
  meta = {"collection": "jsonplaceholderphoto"}
  data = DictField()
