from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class FakeStoreCartModel(Document):
  meta = {"collection": "fakestorecart"}
  data = DictField()
