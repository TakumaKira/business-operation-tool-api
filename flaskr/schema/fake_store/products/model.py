from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class FakeStoreProductModel(Document):
  meta = {"collection": "fakestoreproduct"}
  id = IntField(primary_key=True)
  data = DictField()
