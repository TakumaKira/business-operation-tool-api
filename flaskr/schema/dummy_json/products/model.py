from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class DummyJsonProductModel(Document):
  meta = {"collection": "dummyjsonproduct"}
  id = IntField(primary_key=True)
  data = DictField()
