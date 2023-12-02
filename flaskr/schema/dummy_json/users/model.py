from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class DummyJsonUserModel(Document):
  meta = {"collection": "dummyjsonuser"}
  data = DictField()
