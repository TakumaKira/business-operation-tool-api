from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class JsonPlaceholderTodoModel(Document):
  meta = {"collection": "jsonplaceholdertodo"}
  id = IntField(primary_key=True)
  data = DictField()
