from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class DummyJsonPostModel(Document):
  meta = {"collection": "dummyjsonpost"}
  data = DictField()
