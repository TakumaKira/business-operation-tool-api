from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class DummyJsonCommentModel(Document):
  meta = {"collection": "dummyjsoncomment"}
  data = DictField()
