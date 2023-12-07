from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class JsonPlaceholderPostModel(Document):
  meta = {"collection": "jsonplaceholderpost"}
  id = IntField(primary_key=True)
  data = DictField()
