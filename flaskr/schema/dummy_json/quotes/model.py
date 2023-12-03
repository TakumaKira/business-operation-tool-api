from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class DummyJsonQuoteModel(Document):
  meta = {"collection": "dummyjsonquote"}
  data = DictField()
