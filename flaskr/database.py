from mongoengine import connect
import mongomock

from .schema.fake_store.products.model import FakeStoreProductModel

connect("business-operation-tool", host="mongodb://localhost", mongo_client_class=mongomock.MongoClient)


def init_db():
  pass
