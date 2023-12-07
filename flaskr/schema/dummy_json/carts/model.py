from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class DummyJsonCartModel(Document):
  meta = {"collection": "dummyjsoncart"}
  id = IntField(primary_key=True)
  data = DictField()
