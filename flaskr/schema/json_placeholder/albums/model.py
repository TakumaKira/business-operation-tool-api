from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class JsonPlaceholderAlbumModel(Document):
  meta = {"collection": "jsonplaceholderalbum"}
  data = DictField()
