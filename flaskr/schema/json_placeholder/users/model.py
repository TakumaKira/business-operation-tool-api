from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class JsonPlaceholderUserModel(Document):
  meta = {"collection": "jsonplaceholderuser"}
  id = IntField(primary_key=True)
  data = DictField()
