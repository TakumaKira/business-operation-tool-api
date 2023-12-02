from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class JsonPlaceholderUserModel(Document):
  meta = {"collection": "jsonplaceholderuser"}
  data = DictField()
