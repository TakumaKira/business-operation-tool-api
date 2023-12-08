from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class JsonPlaceholderCommentModel(Document):
  meta = {"collection": "jsonplaceholdercomment"}
  id = IntField(primary_key=True)
  data = DictField()
