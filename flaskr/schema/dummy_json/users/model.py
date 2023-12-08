from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class DummyJsonUserModel(Document):
  meta = {"collection": "dummyjsonuser"}
  id = IntField(primary_key=True)
  data = DictField()
