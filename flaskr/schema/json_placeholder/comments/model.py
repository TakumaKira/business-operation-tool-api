from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class JsonPlaceholderCommentModel(Document):
  meta = {"collection": "jsonplaceholdercomment"}
  data = DictField()
