from mongoengine import Document
from mongoengine.fields import (
  DictField,
)


class FakeStoreUserModel(Document):
  meta = {"collection": "fakestoreuser"}
  data = DictField()
