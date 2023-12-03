from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class DummyJsonCartModel(Document):
  meta = {"collection": "dummyjsoncart"}
  data = DictField()
