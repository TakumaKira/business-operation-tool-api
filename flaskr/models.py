from mongoengine import Document
from mongoengine.fields import (
  DictField,
)

class FakeStoreProduct(Document):
  meta = {"collection": "fakestoreproduct"}
  data = DictField()
