from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class DummyJsonTodoModel(Document):
  meta = {"collection": "dummyjsontodo"}
  data = DictField()
