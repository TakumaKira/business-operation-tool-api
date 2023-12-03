from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class DummyJsonProductModel(Document):
  meta = {"collection": "dummyjsonproduct"}
  data = DictField()
