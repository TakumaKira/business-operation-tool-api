from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class DummyJsonPostModel(Document):
  meta = {"collection": "dummyjsonpost"}
  id = IntField(primary_key=True)
  data = DictField()
