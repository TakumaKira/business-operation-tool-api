from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class FakeStoreCartModel(Document):
  meta = {"collection": "fakestorecart"}
  id = IntField(primary_key=True)
  data = DictField()
