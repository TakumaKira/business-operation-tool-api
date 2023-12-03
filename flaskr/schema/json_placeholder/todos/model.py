from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class JsonPlaceholderTodoModel(Document):
  meta = {"collection": "jsonplaceholdertodo"}
  data = DictField()
