from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class DummyJsonCommentModel(Document):
  meta = {"collection": "dummyjsoncomment"}
  id = IntField(primary_key=True)
  data = DictField()
