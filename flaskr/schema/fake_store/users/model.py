from mongoengine import Document
from mongoengine.fields import (
  DictField,
  IntField,
)


class FakeStoreUserModel(Document):
  meta = {"collection": "fakestoreuser"}
  id = IntField(primary_key=True)
  data = DictField()
