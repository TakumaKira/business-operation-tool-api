from mongoengine import connect
import mongomock

connect("business-operation-tool", host="mongodb://localhost", mongo_client_class=mongomock.MongoClient)


def init_db():
  pass
