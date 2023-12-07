from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class DummyJsonTodoModel(Document):
  meta = {"collection": "dummyjsontodo"}
  id = IntField(primary_key=True)
  data = DictField()
