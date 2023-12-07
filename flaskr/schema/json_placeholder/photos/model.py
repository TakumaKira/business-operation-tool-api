from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class JsonPlaceholderPhotoModel(Document):
  meta = {"collection": "jsonplaceholderphoto"}
  id = IntField(primary_key=True)
  data = DictField()
