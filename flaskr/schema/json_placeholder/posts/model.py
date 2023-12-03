from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class JsonPlaceholderPostModel(Document):
  meta = {"collection": "jsonplaceholderpost"}
  data = DictField()
