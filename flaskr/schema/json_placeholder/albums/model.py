from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class JsonPlaceholderAlbumModel(Document):
  meta = {"collection": "jsonplaceholderalbum"}
  id = IntField(primary_key=True)
  data = DictField()
