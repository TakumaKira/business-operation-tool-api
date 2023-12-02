from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class FakeStoreProductModel(Document):
  meta = {"collection": "fakestoreproduct"}
  data = DictField()
